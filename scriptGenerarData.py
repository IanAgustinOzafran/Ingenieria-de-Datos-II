import json
from faker import Faker
import random

# Inicializar Faker
fake = Faker()
generos_musicales = ['Rock', 'Pop', 'Jazz', 'Reggaeton', 'Hip-Hop', 'Clásica', 'Electrónica', 'Indie', 'Trap', 'Funk']

# Generar artistas
def generar_artistas(cantidad):
    artistas = []
    for i in range(cantidad):
        artista = {
            'nombre': fake.first_name(),
            'apellido': fake.last_name(),
            'pais_origen': fake.country(),
        }
        artistas.append(artista)
    return artistas

# Generar un álbum asociado a un artista dado
def generar_album(artista):
    return {
        'titulo': fake.sentence(nb_words=random.randint(1,4)).replace('.', ''),
        'anio_lanzamiento': random.randint(1980, 2024),
        'genero': random.choice(generos_musicales),
        'artista': artista,
        'canciones': [{'nombre': fake.sentence(nb_words=random.randint(1, 4)).replace('.', ''), 'duracion': f"{random.randint(2, 5)}:{random.randint(0, 5)}{random.randint(0, 9)}"} for _ in range(random.randint(5, 15))]
    }
    
# Insertar álbumes
def insertar_albumes_por_artistas(num_artistas=10, num_albumes=4):
    artistas = generar_artistas(num_artistas)
    albumes = []

    for i in range(num_albumes):
        album = generar_album(random.choice(artistas))
        albumes.append(album)

    return albumes
    
# Ejecutar
insertar_albumes_por_artistas(10, 20)  # 10 artistas, 20 álbumes 

with open('musica.json', 'w') as file:
    albumes = insertar_albumes_por_artistas(10, 20)
    json.dump(albumes, file, indent=4)
    file.close()

with open ('musica.json', 'r') as file:
    data = json.load(file)
    
    for musica in data:
        print(f"Artista: {musica['artista']['nombre']} {musica['artista']['apellido']}")
        print(f"Álbum: {musica['titulo']}")
        print(f"Año de lanzamiento: {musica['anio_lanzamiento']}")
        print(f"Género: {musica['genero']}")
        print("Canciones:")
        for cancion in musica['canciones']:
            print(f" - {cancion['nombre']} ({cancion['duracion']})")
        print("\n")
    
    file.close()
    
