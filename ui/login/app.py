from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongodb-service:27017/")  

db = client["login_db"]
collection = db["users"]


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('login_ui.html')
if __name__ == '__main__':
    app.run(port=5000,debug=True)
