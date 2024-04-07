from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongodb-service:27017/")  

db = client["login_db"]
collection = db["users"]


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('order.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if collection.find_one({'username': username}):
            return jsonify({'message': 'Username already exists!'}), 400
        else:
            return jsonify({'message':'User dosent exsits please signup'})

    return render_template('hello.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if collection.find_one({'username': username}):
            return jsonify({'message': 'Username already exists!'}), 400

        user = {'username': username, 'password': password}
        collection.insert_one(user)

        return jsonify({'message': 'User registered successfully!'})

    return render_template('hello.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
