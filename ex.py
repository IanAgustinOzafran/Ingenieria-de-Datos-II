from pymongo import MongoClient

print("hola")

# Conexión a MongoDB (reemplaza con tu URL de conexión si usas MongoDB Atlas)
client = MongoClient("mongodb://localhost:27017/")

# Seleccionar la base de datos
db = client["miBaseDeDatos"]

# Seleccionar una colección
coleccion = db["usuarios"]

# Insertar un documento de ejemplo
documento = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
resultado = coleccion.insert_one(documento)
print(f"Documento insertado con ID: {resultado.inserted_id}")

# Consultar documentos
for doc in coleccion.find({"nombre": "Nico"}, {"_id": 0}):
    print(doc)
print("\nDocumentos en la colección:")
# Mostrar todas las colecciones en la base de datos
for coleccion in db.list_collection_names():
    print("\t-"+coleccion)

