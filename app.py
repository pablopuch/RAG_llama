import gradio as gr
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain import hub
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

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
    api_key = "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"
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

# Función que ejecuta la pregunta y obtiene la respuesta
def chat_with_pdf(history, question):
    # 1. Cargar documentos desde la carpeta especificada
    
    folder_path = "doc"  # Cambia esto por la ruta de tu carpeta
    
    data = load_documents(folder_path)
    
    # 2. Dividir en fragmentos
    all_splits = split_text(data)
    
    # 3. Crear el vectorstore
    vectorstore = create_vectorstore(all_splits)
    
    # 4. Cargar el prompt
    prompt = load_prompt()
    
    # 5. Configurar el LLM
    llm = configure_llm()
    
    # 6. Configurar la cadena de QA
    qa_chain = create_qa_chain(llm, vectorstore, prompt)
    
    # 7. Obtener la respuesta a la pregunta
    result = qa_chain({"query": question})
    
    # 8. Actualizar el historial de la conversación
    history.append((question, result["result"]))
    return history, history

# Configurar la interfaz con Gradio
def main():
    # Configuración de la interfaz de chat
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        state = gr.State([])  # Mantener el historial de la conversación

        with gr.Row():
            with gr.Column(scale=8):  # Ajuste de 'scale' a un valor entero
                txt_input = gr.Textbox(show_label=False, placeholder="Escribe tu pregunta aquí...")
            with gr.Column(scale=1):
                submit_btn = gr.Button("Enviar")
        
        submit_btn.click(chat_with_pdf, inputs=[state, txt_input], outputs=[chatbot, state])
        txt_input.submit(chat_with_pdf, inputs=[state, txt_input], outputs=[chatbot, state])

    demo.launch()

if __name__ == "__main__":
    main()
