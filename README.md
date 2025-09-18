# 📘 Guía de instalación y ejecución en local

Este repositorio contiene la implementación de un sistema modular basado en microservicios para interactuar con gemelo digital de Don Quijote de la Mancha basado en modelos de lenguaje (LLM).  
La arquitectura incluye:

    - Servidor Web (Node/Express): interfaz de usuario (Front-End).  
    - API (FastAPI): gestión de consultas y comunicación con el LLM.  
    - Servidor de inferencias (Ollama): ejecución del modelo en CPU.  

A continuación se explica cómo instalar y ejecutar el sistema de Servidor Web + API + Servidor de inferencias (Ollama) en un entorno local.

## 📦 Requisitos previos

```bash
SO - Linux, macOS o Windows 
Node.js >= 20
Python >= 3.11
Ollama instalado
ChromaDB instalado
Miniconda instalado
````

## 📂 Clonar repositorio

```bash
git clone https://github.com/XMoraP/tfg-xmorap.git
cd tfg-xmorap
```

## 🌐 Servidor Web

```bash
cd web-server
npm install
npm start
```

Acceso:

```bash
http://localhost:3000
```

## ⚙️ API

```bash
cd api-IA-v1.0.0
conda env create -f environment.yml
conda activate api-HistoTwin
python3 apy.py
```

## 🤖 Servidor de inferencias (Ollama)
Activación:

```bash
ollama serve
```
Descarga de modelos:

```bash
ollama run llama3.2
ollama run xmorap/llama3.2-3B-finetuned
```
Verificación de modelos:

```bash
ollama list
```
## 🧪 Comprobación

Acceso web:

```bash
http://localhost:3000
```

Acceso API:

```bash
http://localhost:8000/<Endpoint>
```
Ollama modelo:

```bash
ollama run <modelo>
```
## Licencia
Este proyecto está licenciado bajo la [MIT License](./LICENSE).

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
