from flask import Flask , jsonify
import json
import utlis

app = Flask(__name__)



@app.get('/')
def home():
    return "Home Page"

@app.get('/football')
def get_products():
    with open('football.json','r') as file:
        data = json.load(file)
        # print(data)
        return data["data"]["products"]
    

@app.get('/total-product')
def get_total_product_count():
    with open('football.json','r') as file:
        data = json.load(file)
        # print(data)
        return jsonify(data["data"]["total_products"])
    
@app.get('/max-price')
def method_name():
    data = utlis.read_file()
    # for single_product in data["data"]["products"]:
    #     print(single_product)
    products_data = data.get("data", {}).get("products", [])

    # Return the data as JSON
    return jsonify(products_data)

def convert_price_to_float(price):
    try:
        return float(price)
    except ValueError:
        return 0.0

@app.get('/price')
def get_max_price():
    data = utlis.read_file()
    products_data = data.get("data", {}).get("products", [])

    if not products_data:
        return jsonify({"error": "No products found"})

    # Define the convert_price_to_float function before using it
    max_price_product = max(products_data, key=lambda x: convert_price_to_float(x.get('product_price', '0')))

    # Return the product with the maximum price as JSON
    return jsonify(max_price_product)
    






if __name__=='__main__':
    app.run(debug=True)