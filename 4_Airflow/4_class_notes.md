## Orquestación con Airflow

**Apache Airflow**

![Alt text](image-1.png)

Ventajas y desventajas

![Alt text](image-2.png)

### Resumen de read.ia


En la reunión se presentaron dos herramientas: Orque y Apache. Orque es una herramienta para automatizar flujos de trabajo y se discutió cómo se pueden construir gráficos dirigidos para representar procesos y automatizar tareas. Por otro lado, se presentó Apache como una herramienta para Big Data, destacando su capacidad para desarrollar y supervisar programas de manera escalable y flexible.

Además, se discutieron temas como la integración con aplicaciones externas, la automatización de procesos, la monitorización de proyectos y la importancia de la infraestructura y la organización para la implementación exitosa de estas herramientas. También se discutió sobre la creación de tareas y vinculación de operadores, la dependencia entre tareas y el modelo de regresión lineal, explicando cómo se preparan los datos y cómo se entrena el modelo con datos categóricos.

### Mis notas

Apache Airflow es una herramienta gratuita porque es financiada por la fundación Apache. Se utiliza para orquestación de flujos de trabajo.

**¿Qué es un workflow?**

- Es una secuencia de tareas donde a partir de una actividad se desprende otra o otras.

- Se puede utilizar para crear flujos de trabajos (grafos asiclicos de trabajo). 

![Alt text](image.png)


Para crear diagramas rapidos: diagram.net

![Alt text](image-5.png)

Muchas aplicaciones tienen sus servicios sobre esta aplicación

Apache spark motor para data

Se trata de configurar flujos de trabajo de forma programada. Sus herramientas se manejan a través de una pagina web y un notebook de python.

Tiene workers: Para ejecución de tareas.

Depende en gran medida de Python y el conocimiento de su infraestructura.

Pueden haber problemas de compatibilidad con versiones de Python

Cada tarea se realiza con un operador y pueden ser: un Python operator, Bash operator y otros.

---

## Actividad  

---


### Data pipeline workflow

Asi se ve un ui

![Alt text](image-3.png)
 

Asi se ve un grafo de algun projecto

![Alt text](image-4.png)

---

**Comandos**

``` bash
# Update the package list on your system
sudo apt update

# Install Python 3 package manager (pip)
sudo apt install python3-pip

# Install SQLite database management system
sudo apt install sqlite3

# Install Python 3.10 virtual environment
sudo apt install python3.10-venv

# Install development files for PostgreSQL, required for Python packages like psycopg2
sudo apt-get install libpq-dev

# Activate the Python virtual environment (assuming it was previously created)
source venv/bin/activate

# Install Apache Airflow version 2.5.0 with PostgreSQL support
# and apply constraints for Python 3.7 from a specific URL
pip install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"

# Initialize the Airflow database
airflow db init

# Install PostgreSQL and related contrib packages
sudo apt-get install postgresql postgresql-contrib

# Switch to the PostgreSQL user
sudo -i -u postgres

# Start the PostgreSQL interactive terminal
psql

# Create a PostgreSQL database named "airflow"
CREATE DATABASE airflow;

# Create a PostgreSQL user named "airflow" with the password 'airflow'
CREATE USER airflow WITH PASSWORD 'airflow';

# Grant all privileges on the "airflow" database to the "airflow" user
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

# Update the Airflow configuration to use PostgreSQL instead of SQLite
sed -i 's#sqlite:////home/oscar_rincon/code/oscar-rincon/ml-engineering-course/airflow/airflow.db#postgresql+psycopg2://airflow:airflow@localhost/airflow#g' airflow.cfg

# Modify the Airflow configuration to use the LocalExecutor instead of the SequentialExecutor
sed -i 's#SequentialExecutor#LocalExecutor#g' airflow.cfg

# Reinitialize the Airflow database with the updated configuration
airflow db init

# Create an Airflow admin user
airflow users create -u airflow -f airflow -l airflow -r Admin -e airflow@gmail.com

# Start the Airflow web server in the background
airflow webserver &

# Start the Airflow scheduler
airflow scheduler

# List running processes and find the Airflow web server process ID (replace 1234 with the actual PID)
ps aux | grep airflow

# Terminate the Airflow web server by killing its process (replace 1234 with the actual PID)
kill 1234

```