import requests
from flask import Flask, render_template
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch JSON data from the API
    api_url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
    response = requests.get(api_url)
    data = response.json()

    # Extract products from the data
    products = data.get('products', {})

    # Convert popularity values to integers
    for product_id, product_info in products.items():
        product_info['popularity'] = int(product_info['popularity'])

    # Sort data based on descending popularity
    sorted_data = sorted(products.values(), key=lambda x: x['popularity'], reverse=True)

    return render_template('index.html', products=sorted_data)

if __name__ == '__main__':
    app.run(debug=True)
