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

### 1. Clonar el Repositorio

Clona el repositorio desde GitHub en tu máquina local:

```bash
git clone https://github.com/pablopuch/RAG_llama.git
cd RAG_llama


### 2. Crear y Activar un Entorno Virtual

Es recomendable utilizar un entorno virtual para aislar las dependencias del proyecto:

En Windows:

```bash
python -m venv env
.\env\Scripts\activate

En macOS/Linux:

python3 -m venv env
source env/bin/activate

