from flask import Flask, request, jsonify, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongodb-service:27017/")  

db = client["login_db"]
collection = db["users"]

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_document = collection.find_one({'username': username})
        if user_document:
            # Convert ObjectId to string
            user_document['_id'] = str(user_document['_id'])
            # Extract userID from the user_document
            userID = user_document['userID']
            # Redirect to /products with userID as a query parameter
            return redirect(f'http://localhost:5004/products?userID={userID}')
        else:
            return jsonify({'message': 'User does not exist, please sign up'})

    return render_template('hello.html')


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if collection.find_one({'username': username}):
            return jsonify({'message': 'Username already exists!'}), 400
        
        # Get the maximum userID
        max_user = collection.find_one(sort=[("userID", -1)])
        if max_user:
            userID = max_user["userID"] + 1
        else:
            userID = 1
        user = {'userID': userID, 'username': username, 'password': password}
        collection.insert_one(user)

        return render_template('hello.html')

    return render_template('hello.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
