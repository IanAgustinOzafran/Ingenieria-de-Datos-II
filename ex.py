from pymongo import MongoClient

# Conectar a MongoDB (cambia la URI si usas un servidor remoto)
client = MongoClient("mongodb://localhost:27017/")

# Obtener la lista de bases de datos disponibles
db_list = client.list_database_names()

# Mostrar las bases de datos
print("Bases de datos en MongoDB:")
for db in db_list:
    print(f"- {db}")

# Cerrar la conexión
client.close()

