import json

with open('musica.json', 'r') as file:
    data = json.load(file)
    for musica in data:
        print(f"Artista: {musica['artista']}, Álbum: {musica['album']}, Genero: {musica['genero']}")

