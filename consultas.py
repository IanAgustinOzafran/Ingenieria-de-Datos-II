from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
 
db = client["TPO"]
 
musica_collection = db["Musica"]

print("\n" + "-" * 50 + "\n")
# Consulta 1: Encontrar albumes lanzados entre 2000 y 2010
print("Álbumes lanzados entre 2000 y 2010:")
print("--------------------------------------------------")
albums_in_range = musica_collection.find({"anio_lanzamiento": {"$gte": 2000, "$lte": 2010}},
{"_id": 0, "titulo": 1, "artista": 1, "anio_lanzamiento": 1, "genero": 1})
for album in albums_in_range:
    print(album)

print("\n" + "-" * 50 + "\n")

# Consulta 2: Encontrar un documento con un título específico
titulo_especifico = musica_collection.find_one({"titulo": "Option"})
if titulo_especifico:
    print(f"Documento encontrado: Título: {titulo_especifico.get('titulo', 'Desconocido')}, "
          f"Artista: {titulo_especifico.get('artista', 'Desconocido')}, "
          f"Año: {titulo_especifico.get('anio_lanzamiento', 'Desconocido')}, "
          f"Género: {titulo_especifico.get('genero', 'Desconocido')}")
else:
    print("No se encontró ningún documento con el título especificado.")

print("\n" + "-" * 50 + "\n")

# Consulta 3: Listar todos los documentos con un género específico
genero_especifico = musica_collection.find({"genero": "Rock"})
print("Documentos con género 'Rock':")
for i, doc in enumerate(genero_especifico, start=1):
    print(f"{i}. Título: {doc.get('titulo', 'Desconocido')}, Artista: {doc.get('artista', 'Desconocido')},Año: {doc.get('anio_lanzamiento', 'Desconocido')}")

print("\n" + "-" * 50 + "\n")

# Consulta 4: Obtener los 5 documentos más recientes según el año de lanzamiento
documentos_recientes = musica_collection.find().sort("anio_lanzamiento", -1).limit(5)
print("Los 5 documentos más recientes según el año de lanzamiento:")
for i, doc in enumerate(documentos_recientes, start=1):
    print(f"{i}. Título: {doc.get('titulo', 'Desconocido')}, Año: {doc.get('anio_lanzamiento', 'Desconocido')}")

print("\n" + "-" * 50 + "\n")

# Consulta 5: Agrupar por género y contar la cantidad de canciones en cada género
agrupacion_por_genero = musica_collection.aggregate([
    {"$group": {"_id": "$genero", "cantidad": {"$sum": 1}}},
    {"$sort": {"cantidad": -1}}
])
print("Cantidad de canciones por género:")
for grupo in agrupacion_por_genero:
    print(grupo)