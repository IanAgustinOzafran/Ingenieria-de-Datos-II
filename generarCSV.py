import pandas as pd
from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")

db = client["TPO"]

musica_collection = db["Musica"]




albumes = musica_collection.find({},{"_id": 0})
df = pd.DataFrame(list(albumes))
df.to_csv('musica.csv', index=False)
print("\n" + "-" * 50 + "\n")
print("Los datos han sido exportados a musica.csv")