# Ingenieria-de-Datos-II
TPO - Motor de Base de Datos MongoDB con Aplicación de Software Python 

Objetivo:
● Aprender a conectar MongoDB con Python. 
● Practicar operaciones CRUD en MongoDB usando Python. 
● Explorar consultas avanzadas y manipulación de datos con PyMongo. 
● Aplicar conocimientos en un caso práctico real. 
● Evidenciar cada uno de los puntos solicitados como enunciado.

Requisitos previos 
1. MongoDB instalado (incluyendo MongoDB Shell y Compass). 
2. Python instalado con la librería pymongo. 
Se instala con: pip install pymongo 
3. Un dataset a elección como propuesta del equipo de trabajo JSON para 
cargar en MongoDB.

Enunciado: 

Parte 0: Entorno de Trabajo: Instalación 
Evidenciar en qué contexto se trabajará tanto para MongoDB, como Python (Notebook con políticas de seguridad, sistema operativo, etc., es decir, tomar en cuenta los aspectos y feedback mencionados en la clase sobre la instalación de MongoDB). 

Parte 1: Instalación y Conexión de MongoDB con Python 
Conectar Python con MongoDB 
1) Crear un script en Python que establezca una conexión con MongoDB y liste las bases de datos disponibles. 
2) Crear una base de datos y una colección en base a la propuesta del equipo.

Parte 2: Cargar y Consultar Datos en MongoDB 
3) Insertar documentos en la colección (manualmente). 
4) Consultar todos los documentos realizados. 
5) Realizar 7 propuestas de filtros sobre los documentos trabajados. 

Parte 3: Actualizar y Eliminar Datos 
6) Realizar 7 propuestas de actualización sobre los documentos trabajados. 
7) Realizar 7 propuestas de eliminación sobre los documentos trabajados. 
NOTA:Tener en cuenta la aplicación de “filtros”. 

Parte 4: Proyecto Final - Análisis de Datos en MongoDB 
Caso práctico: 
8) Investigar herramientas de autogeneración de datos a través de Script para simulación de datos en MongoDB. El mismo se deberá dejar como evidencia en la entrega bajo un archivo TemaSeleccionadoPorElGrupo.json (dataset ficticio).  
Una vez realizado dicho paso, se deberá:  
● Cargar el archivo JSON en MongoDB. 
Se puede hacer desde MongoDB Compass o con Python:

9) Sobre dichos datos generados (tema a elección del equipo de trabajo), se deberá 
realizar la propuesta de 5 consultas, por ejemplo del tipo: 
a) Listar empleados mayores de 30 años con salario superior a 7000. 
b) Contar cuántos empleados hay en cada cargo. 
c) Obtener el promedio de salario por cargo.

10) Exportar los resultados a un archivo CSV, y mostrar habilidades con manejo de 
pandas de python, por ejemplo: Usar pandas para guardar la salida en CSV.

Entrega del TPO 
Cada equipo deberá subir un informe en formato PDF con: 
● Código utilizado en Python. 
● Capturas de pantalla de MongoDB Compass mostrando los datos. 
● Resultados de las consultas y análisis realizados. 

EXTRA: Conexión de MongoDB con una API y Dashboard 
Objetivo: 
● Crear una API en Flask para exponer los datos de MongoDB. 
● Consumir los datos desde un dashboard en Power BI o Tableau. 
Paso a paso: 
