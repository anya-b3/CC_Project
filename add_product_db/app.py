from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongodb-service:27017/")  

db = client["product_db"]
collection = db["products"]

@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        # Get data from request
        data = {'Name':'Lays','Price':'$5','Description':'Crunchy,Fatty'}
        
        # Insert data into MongoDB
        result = collection.insert_one(data)

        return jsonify({"message": "Product added successfully", "product_id": str(result.inserted_id)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
