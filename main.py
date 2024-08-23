from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import gradio as gr
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain import hub
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

api_key = os.getenv('API_KEY')

app = FastAPI()

# Modelos de datos para la API
class QuestionRequest(BaseModel):
    question: str
    history: list = []

# Cargar el contenido de todos los archivos PDF en una carpeta
def load_documents(folder_path):
    all_documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            loader = PyPDFLoader(os.path.join(folder_path, filename))
            all_documents.extend(loader.load())
    return all_documents

# Dividir el texto en fragmentos
def split_text(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    return text_splitter.split_documents(data)

# Crear el vectorstore a partir de los fragmentos de texto
def create_vectorstore(splits):
    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    return Chroma.from_documents(documents=splits, embedding=embeddings)

# Descargar el prompt de RAG
def load_prompt():
    return hub.pull("rlm/rag-prompt-llama", api_key=api_key)

# Configurar el modelo de lenguaje Llama3.1 con Ollama
def configure_llm():
    return Ollama(model="llama3.1:latest", verbose=True)

# Configurar la cadena de preguntas y respuestas con recuperación
def create_qa_chain(llm, vectorstore, prompt):
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )

# Preparar el entorno una vez al iniciar la aplicación
folder_path = "doc"  # Cambia esto por la ruta de tu carpeta
data = load_documents(folder_path)
all_splits = split_text(data)
vectorstore = create_vectorstore(all_splits)
prompt = load_prompt()
llm = configure_llm()
qa_chain = create_qa_chain(llm, vectorstore, prompt)

# API para manejar la pregunta y devolver la respuesta
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        # Obtener la respuesta a la pregunta
        result = qa_chain({"query": request.question})
        
        # Actualizar el historial de la conversación
        request.history.append((request.question, result["result"]))
        
        return {"history": request.history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para la interfaz Gradio
@app.get("/gradio")
def get_gradio_interface():
    async def chat_with_pdf(history, question):
        request = QuestionRequest(question=question, history=history)
        result = await ask_question(request)
        return result["history"], result["history"]

    # Crear la interfaz de Gradio
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        state = gr.State([])  # Mantener el historial de la conversación

        with gr.Row():
            with gr.Column(scale=8):
                txt_input = gr.Textbox(show_label=False, placeholder="Escribe tu pregunta aquí...")
            with gr.Column(scale=1):
                submit_btn = gr.Button("Enviar")
        
        submit_btn.click(chat_with_pdf, inputs=[state, txt_input], outputs=[chatbot, state])
        txt_input.submit(chat_with_pdf, inputs=[state, txt_input], outputs=[chatbot, state])

    return demo.launch(inline=True)
