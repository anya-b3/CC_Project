from flask import Flask, request, jsonify, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongodb-service:27017/") 

db = client["product_db"]
collection = db["products"]
cart_collection = db["cart"]  # Collection for user's cart


@app.route('/products', methods=['GET'])
def get_products():
    # Get the userID from the query parameters
    global userID
    userID = request.args.get('userID')
    print("UserID:", userID)


    products = []
    for product in collection.find():
        products.append(product)
        print(product)
    return render_template('product.html', products=products)

@app.route('/', methods=['POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('price'))  # Convert price to float
        description = request.form.get('description')

        product = {'Name': name, 'Price': price, 'Description': description}
        collection.insert_one(product)
        print(product)

        return jsonify({'message': 'Product added successfully!'})

    return render_template('product.html')  # Redirect to products page on error

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        # userID = request.args.get('userID')  # Get userID from query parameters
        product_id = request.form.get('product_id')  # Get product_id from form data
        product_name = request.form.get('product_name')

        # Create entry for user's cart
        cart_entry = {'userID': userID, 'product_id': product_id, 'product_name': product_name}
        result = cart_collection.insert_one(cart_entry)

        if result.acknowledged:
            # Convert ObjectId to string
            # cart_entry['_id'] = str(cart_entry['_id'])
            # return jsonify({'message': 'Item added to cart successfully!', 'cart_entry': cart_entry}), 200
            return redirect(f'http://localhost:5004/products?userID={userID}')

        else:
            return jsonify({'error': 'Failed to add item to cart!'}), 500

    return jsonify({'error': 'Invalid request'}), 400

@app.route('/order',methods=['POST','GET'])
def change_to_order():
    return redirect(f'http://localhost:5003/?userID={userID}')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
