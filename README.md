# Proyecto RAG con Modelo LLM Llama 3.1 e Interfaz Gradio

Este proyecto implementa un sistema de Recuperación de Información con Generación de Respuestas (RAG) utilizando el modelo Llama 3.1. Permite realizar preguntas sobre archivos PDF que se encuentren en una carpeta específica y obtener respuestas utilizando un modelo LLM. El proyecto incluye tres componentes:

1. **Consola**: Interacción con el modelo desde la línea de comandos.
2. **Interfaz Gradio**: Interfaz gráfica interactiva para realizar preguntas y obtener respuestas.
3. **API FastAPI**: Provee un endpoint para interactuar con el modelo desde cualquier frontend.

## Contenido del Repositorio

- `llama_console.py`: Script para interactuar con el modelo Llama 3.1 desde la consola.
- `llama_gradio.py`: Interfaz Gradio para interactuar con el modelo.
- `llama_api.py`: API construida con FastAPI que expone un endpoint para interactuar con el modelo.

## Requisitos Previos

- **Python 3.8 o superior**
- **Git**
- **Virtualenv** (opcional, pero recomendado)

## Instalación

Sigue estos pasos para instalar y configurar el proyecto en tu entorno local.

## 1. Clonar el Repositorio

Clona el repositorio desde GitHub en tu máquina local:

```bash
git clone https://github.com/pablopuch/RAG_llama.git
cd RAG_llama
```

## 2. Crear y Activar un Entorno Virtual

Es recomendable utilizar un entorno virtual para aislar las dependencias del proyecto:

En Windows:

```bash
python -m venv env
.\env\Scripts\activate
```

En macOS/Linux:

```bash
python3 -m venv env
source env/bin/activate
```

## 3. Instalar las Dependencias

Instala todas las dependencias necesarias utilizando pip. El archivo requirements.txt contiene todas las librerías requeridas.

```bash
pip install -r requirements.txt
```

## 4. Configurar la API Key de LangChain

El proyecto utiliza la API de LangChain para descargar el prompt. Necesitarás configurar tu API key en el entorno virtual. En tu sistema operativo, puedes establecer variables de entorno de manera manual.

Configura la API Key como una variable de entorno:

En Windows:

```bash
setx API_KEY "tu_api_key_aqui"
```
En macOS/Linux:

```bash
export API_KEY="tu_api_key_aqui"
```

## 5. Crear la Carpeta de Documentos

Crea una carpeta llamada doc en la raíz del proyecto. Coloca todos los archivos PDF con los que quieras trabajar dentro de esta carpeta.

```bash
mkdir doc
```


## Ejecución

Sigue estos pasos para instalar y configurar el proyecto en tu entorno local.

## 1. Ejecutar el Script de Consola

Para ejecutar el script que interactúa con el modelo desde la consola,Este script te permitirá hacer preguntas sobre los archivos PDF que has colocado en la carpeta doc.

Utiliza el siguiente comando:

```bash
py  llama_console.py
```
## 2. Ejecutar la Interfaz Gradio

Para lanzar la interfaz Gradio y hacer preguntas de manera interactiva. Esto abrirá una interfaz web donde podrás interactuar con el modelo de manera gráfica.

Ejecuta:

```bash
py  llama_console.py
```
## 3. Ejecutar la API con FastAPI

Para levantar la API y exponer un endpoint para interacción desde cualquier frontend. La API estará disponible en http://127.0.0.1:8000. Puedes acceder a la documentación automática generada por FastAPI en http://127.0.0.1:8000/docs. 

Utiliza:

```bash
fastapi dev main.py
```