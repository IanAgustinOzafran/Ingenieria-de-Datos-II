from flask import Flask, jsonify
from pymongo import MongoClient
app = Flask(__name__)
# Conexión con MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["TPO"]
collection = db["Musica"]
@app.route('/Musica', methods=['GET'])

def get_albumes():
    albumes = list(collection.find({}, {"_id": 0})) # Excluye el _id para evitar problemas en JSON
    return jsonify(albumes)

if __name__ == '__main__':
    app.run(debug=True)