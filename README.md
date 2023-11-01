# Introducción a la Ingeniería de Machine Learning

Este repositorio contiene el material del curso "Introducción a la Ingeniería de Machine Learning" que estoy siguiendo como estudiante en la Universidad de Antioquia, bajo la dirección del profesor Santiago Echeverri Valencia (santiago.echeverriv@udea.edu.co). En este curso, exploraremos los conceptos fundamentales de la ingeniería de machine learning, así como las herramientas y técnicas necesarias para desarrollar sistemas de machine learning de manera efectiva.

## Contenido del Curso

El curso se divide en varias secciones, cada una abordando un aspecto clave de la ingeniería de machine learning. Aquí está una descripción general de los temas que se cubrirán:

1. **Fundamentos de Python, Docker, GIT y Línea de Comandos**
   - Introducción a Python y sus aplicaciones en machine learning (Python 3.9 o superior recomendado).
   - Uso de Docker para la creación de entornos aislados.
   - Control de versiones con GIT.
   - Conceptos básicos de líneas de comando.
   - Introducción a modelos supervisados y no supervisados.

2. **MLOps: Gestión de Proyectos de Machine Learning**
   - ¿Qué es MLOps y por qué es importante?
   - Modelo de madurez MLOps.
   - Razones para implementar MLOps en proyectos de machine learning.
   - Visión general del curso.
   - Preparación del entorno de desarrollo (Se recomienda sistemas operativos basados en UNIX como Ubuntu o macOS).

3. **Seguimiento de Experimentos con MLflow**
   - Introducción al seguimiento de experimentos.
   - Utilización de MLflow para el seguimiento de experimentos.
   - Almacenamiento y carga de modelos con MLflow.
   - Registro de modelos y su importancia.
   - Aplicación práctica de MLflow en proyectos reales.

4. **Orquestación con Airflow**
   - Uso de Apache Airflow para orquestar flujos de trabajo.
   - Transformación de cuadernos de Jupyter en flujos de trabajo.
   - Despliegue de flujos de trabajo para una ejecución eficiente.

5. **Despliegue de Modelos en Servicios Web**
   - Diferentes enfoques para el despliegue de modelos.
   - Despliegue de modelos como servicios web utilizando FastAPI.
   
6. **Monitorización de Servicios Basados en Machine Learning**
   - Monitorización de servicios web con herramientas como Prometheus, Evidently y Grafana.
   - Monitorización de trabajos por lotes con Airflow, MongoDB y Evidently.

## Requisitos

Antes de comenzar con el curso, asegúrate de tener instalados los siguientes elementos en tu entorno de desarrollo:

- Python 3.9 o superior
- Docker
- GIT
- Herramientas de MLOps (como MLflow y Apache Airflow)
- FastAPI
- Herramientas de monitorización (como Prometheus, Evidently y Grafana)

## Instrucciones de Uso

Cada sección del curso estará organizada en su propio directorio dentro de este repositorio. Dentro de cada directorio, encontrarás material de lectura, ejemplos de código y ejercicios relacionados con el tema tratado.

Siéntete libre de explorar y utilizar este repositorio para aprender sobre la ingeniería de machine learning.

¡Disfruta del curso! Si tienes alguna pregunta o encuentras problemas, no dudes en abrir un problema o ponerte en contacto con nosotros.

## Contribución

Si deseas contribuir a este curso agregando contenido, corrigiendo errores o mejorando la estructura, te invitamos a hacerlo. ¡Esperamos tus contribuciones!

## Arbol actual del repositorio

``` bash
.
├── 1_Fundamentals
│   └── 1_class_notes.md
├── 2_MLOps
│   ├── 2_class_notes.md
│   └── tutorial.ipynb
├── 3_MLflow
│   ├── 3_class_notes.md
│   ├── automobileEDA.csv
│   ├── automobileEDA.csv:Zone.Identifier
│   ├── image-1.png
│   ├── image-2.png
│   ├── image-3.png
│   ├── image.png
│   ├── main.py
│   └── mlruns
├── 4_Airflow
│   ├── 4_class_notes.md
│   ├── image-1.png
│   ├── image-2.png
│   ├── image-3.png
│   ├── image-4.png
│   ├── image-5.png
│   ├── image.png
│   ├── logs
│   └── primerdag.py
├── 5_Deployment
│   └── 5_class_notes.md
├── 6_Monitoring
│   └── 6_class_notes.md
├── LICENSE
├── README.md
├── airflow
│   ├── airflow
│   ├── airflow-webserver.pid
│   ├── airflow.cfg
│   ├── airflow.db
│   ├── dags
│   ├── logs
│   └── webserver_config.py
├── logs
├── requirements.txt
└── venv
    ├── bin
    ├── etc
    ├── generated
    ├── include
    ├── lib
    ├── lib64 -> lib
    ├── pyvenv.cfg
    └── share

21 directories, 29 files
```
