import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain import hub
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("API_KEY no está configurada correctamente.")

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

# Inicializar el sistema: cargar documentos, crear vectorstore y cadena de QA
def initialize_system(folder_path):
    # 1. Cargar documentos desde la carpeta especificada
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
    
    return qa_chain

# Función para hacer preguntas al sistema preprocesado
def chat_with_pdf(qa_chain, history, question):
    # 7. Obtener la respuesta a la pregunta usando el QA chain
    result = qa_chain({"query": question})
    
    # 8. Actualizar el historial de la conversación
    history.append((question, result["result"]))
    return history, history

if __name__ == "__main__":
    folder_path = "doc"  # Cambia esto por la ruta de tu carpeta
    history = []

    # Inicializar el sistema una vez
    qa_chain = initialize_system(folder_path)
    
    while True:
        # Solicitar una pregunta al usuario
        question = input("Escribe tu pregunta (o 'exit' para salir): ")
        
        if question.lower() == "exit":
            break

        # Obtener la respuesta del modelo usando el sistema ya inicializado
        history, updated_history = chat_with_pdf(qa_chain, history, question)
        
        # Mostrar la respuesta
        print(f"Respuesta: {updated_history[-1][1]}\n")