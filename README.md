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

<div align="center">
 <img alt="ollama" height="200px" src="https://github.com/ollama/ollama/assets/3325447/0d0b44e2-8f4a-4e99-9b52-a5c1c741c8f7">
</div>

# Ollama

Get up and running with large language models.

### macOS

[Download](https://ollama.com/download/Ollama-darwin.zip)

### Windows preview

[Download](https://ollama.com/download/OllamaSetup.exe)

## Quickstart

To run and chat with [Llama 3.1](https://ollama.com/library/llama3.1):

```
ollama run llama3.1
```

## Model library

Ollama supports a list of models available on [ollama.com/library](https://ollama.com/library 'ollama model library')

Here are some example models that can be downloaded:

| Model              | Parameters | Size  | Download                       |
| ------------------ | ---------- | ----- | ------------------------------ |
| Llama 3.1          | 8B         | 4.7GB | `ollama run llama3.1`          |
| Llama 3.1          | 70B        | 40GB  | `ollama run llama3.1:70b`      |
| Llama 3.1          | 405B       | 231GB | `ollama run llama3.1:405b`     |
| Phi 3 Mini         | 3.8B       | 2.3GB | `ollama run phi3`              |
| Phi 3 Medium       | 14B        | 7.9GB | `ollama run phi3:medium`       |
| Gemma 2            | 2B         | 1.6GB | `ollama run gemma2:2b`         |
| Gemma 2            | 9B         | 5.5GB | `ollama run gemma2`            |
| Gemma 2            | 27B        | 16GB  | `ollama run gemma2:27b`        |
| Mistral            | 7B         | 4.1GB | `ollama run mistral`           |
| Moondream 2        | 1.4B       | 829MB | `ollama run moondream`         |
| Neural Chat        | 7B         | 4.1GB | `ollama run neural-chat`       |
| Starling           | 7B         | 4.1GB | `ollama run starling-lm`       |
| Code Llama         | 7B         | 3.8GB | `ollama run codellama`         |
| Llama 2 Uncensored | 7B         | 3.8GB | `ollama run llama2-uncensored` |
| LLaVA              | 7B         | 4.5GB | `ollama run llava`             |
| Solar              | 10.7B      | 6.1GB | `ollama run solar`             |

> [!NOTE]
> You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.

## Customize a model

### Import from GGUF

Ollama supports importing GGUF models in the Modelfile:

1. Create a file named `Modelfile`, with a `FROM` instruction with the local filepath to the model you want to import.

   ```
   FROM ./vicuna-33b.Q4_0.gguf
   ```

2. Create the model in Ollama

   ```
   ollama create example -f Modelfile
   ```

3. Run the model

   ```
   ollama run example
   ```

### Import from PyTorch or Safetensors

See the [guide](docs/import.md) on importing models for more information.

### Customize a prompt

Models from the Ollama library can be customized with a prompt. For example, to customize the `llama3.1` model:

```
ollama pull llama3.1
```

Create a `Modelfile`:

```
FROM llama3.1

# set the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1

# set the system message
SYSTEM """
You are Mario from Super Mario Bros. Answer as Mario, the assistant, only.
"""
```

Next, create and run the model:

```
ollama create mario -f ./Modelfile
ollama run mario
>>> hi
Hello! It's your friend Mario.
```

For more examples, see the [examples](examples) directory. For more information on working with a Modelfile, see the [Modelfile](docs/modelfile.md) documentation.

## CLI Reference

### Create a model

`ollama create` is used to create a model from a Modelfile.

```
ollama create mymodel -f ./Modelfile
```

### Pull a model

```
ollama pull llama3.1
```

> This command can also be used to update a local model. Only the diff will be pulled.

### Remove a model

```
ollama rm llama3.1
```

### Copy a model

```
ollama cp llama3.1 my-model
```

### Multiline input

For multiline input, you can wrap text with `"""`:

```
>>> """Hello,
... world!
... """
I'm a basic program that prints the famous "Hello, world!" message to the console.
```

### Multimodal models

```
ollama run llava "What's in this image? /Users/jmorgan/Desktop/smile.png"
The image features a yellow smiley face, which is likely the central focus of the picture.
```

### Pass the prompt as an argument

```
$ ollama run llama3.1 "Summarize this file: $(cat README.md)"
 Ollama is a lightweight, extensible framework for building and running language models on the local machine. It provides a simple API for creating, running, and managing models, as well as a library of pre-built models that can be easily used in a variety of applications.
```

### Show model information

```
ollama show llama3.1
```

### List models on your computer

```
ollama list
```

### Start Ollama

`ollama serve` is used when you want to start ollama without running the desktop application.


# Ejecución

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