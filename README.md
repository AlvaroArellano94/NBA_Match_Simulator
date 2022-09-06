# NBA_Match_Simulator
Trabjo de fin del Máster de Análisis y Visualización de Datos Masivos

![image](https://user-images.githubusercontent.com/37518023/168859275-cabb8905-933f-48c9-869f-16fa8a08bad4.png)

# Objetivo
El objetivo de este proyecto consiste en generar un Cuadro de Mando consultable en tiempo real que te de información clave sobre un partido de Baloncesto. Para este proyecto, se ha seleccionado un partido de la liga de baloncesto americana, la NBA. 

# Estructura
El proyecto está estructurado en 3 bloques:
  (1)Aplicación desarrollada en Python: el objetivo de esta aplicación será el generar los datos referentes a un partido de baloncesto e insertar esta información en una      base de datos relacional.   
  (2)BBDDs alojada en Microsoft SQL Server: el objetivo de esta base de datos consiste en guardar y organizar los datos sobre el partido de baloncesto. De este modo,          esta información podrá ser consumida posteriormente por una herramienta de reporting. 
  (3)Aplicación utilizando la herramienta de dashboarding PowerBI: el objetivo de esta aplicación consiste en mostrar la información más relevante del partido.  
  
# Consideraciones previas

DOCKER

A continuación, se van a listar todos los elementos que deben estar instalados para que la aplicación fucione correctamente:

El primer elemento que necesitamos es la instalación del contenedor de Docker que contiene la Base de Datos de Microsoft SQL Server. Para tal, se debe ejecutar el siguiente comando en la linea de comando, sustituyendo en el comando aquellos elementos particulares de cada servidor:

docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=yourStrong(!)Password" -p 1433:1433 --name "docker_container_name" --hostname "host_name"  -d mcr.microsoft.com/mssql/server:2019-latest 

Podemos ver que el contenedor utilizado hace referencia a la última versión del 2019. 
**Cabe destacar que en el 2022 se ha liberado una nueva versión, pero en el desarrollo de este proyecto se ha utilizado la versión de 2019.

PYTHON
Instalación módulo "numpy":
pip3 install numpy
(https://numpy.org/install/)

pip3 install pypyodbc
(https://pypi.org/project/pypyodbc/)

pip3 install pandas
(https://pandas.pydata.org/docs/getting_started/install.html)

pip install python-dotenv
(https://pypi.org/project/python-dotenv/)

# Orden de Ejecución

Ejecución de ficheros SQL:
  (1)Create_DB.sql
  (2)Create_Tables_NBA_Match_Simulator.sql
  (3)Insert_Data_1_app.sql
  (4)Insert_Data_2_app.sql

