from flask import Flask, jsonify
from models import Product
from app import app

products = [
    {
        'id': 1,
        'title': 'Product 1',
        'description': 'This is very awesome and weights a lot',
        'price_per_unit': 10,
        'quantity': 20,
        'unit': 'kilogram'
    },
    {
        'id': 2,
        'title': 'Product 2',
        'description': 'This is quite cool and weights a bit',
        'price_per_unit': 20,
        'quantity': 200,
        'unit': 'gram'
    },
    {
        'id': 3,
        'title': 'Product 3',
        'description': 'This product is plain and simple',
        'price_per_unit': 5,
        'quantity': 20,
        'unit': 'litre'
    }
]

inquiries = [
    {
        'id': 1,
        'products': products[0:2]
    },
    {
        'id': 2,
        'products': products[0:3]
    },
]

offers = [
    {
    'id': 1,
    'products': products[0:2],
    'shipping_form': 'personal',
    'due_date': '01/01/2015',
    'total_value': sum(p['price_per_unit'] * p['quantity'] 
                        for p in products[0:2])
    },
]

@app.route('/')
def index():
    message = "This is a REST api for inquiries and offer management"
    return jsonify({'message': message})


@app.route('/get_products')
def get_products():
    # UC-008 przegladaj katalog s.37
    products = [p.title for p in Product.query.all()]
    return jsonify({'products': products})


@app.route('/add_product_to_inquiry/<int:inquiry_id>')
def add_product_to_inquiry(inquiry_id):
    # UC-009 dodaj produkt do zapytania ofertowego s.37
    if inquiry_id > 0:
        message = 'Adding product to inquiry ' + str(inquiry_id)
    else:
        message = 'Invalid inquiry_id'

    return jsonify({'message': message})


@app.route('/remove_product_from_inquiry/<int:inquiry_id>')
def remove_product_from_inquiry(inquiry_id):
    # UC-011 usun produkt z zapytania ofertowego s.37
    if inquiry_id > 0:
        message = 'Removing product from inquiry ' + str(inquiry_id)
    else:
        message = 'Invalid inquiry_id'

    return jsonify({'message': message})


@app.route('/submit_inquiry/<int:inquiry_id>')
def submit_inquiry(inquiry_id):
    # UC-010 zloz zapytanie ofertowe s.37
    if inquiry_id > 0:
        message = 'Submitting inquiry ' + str(inquiry_id)
    else:
        message = 'Invalid inquiry_id'

    return jsonify({'message': message})


@app.route('/accept_inquiry/<int:inquiry_id>')
def accept_inquiry(inquiry_id):
    # UC-048 przyjmij zapytanie ofertowe s.95
    if inquiry_id > 0:
        message = 'Accepting inquiry ' + str(inquiry_id)
    else:
        message = 'Invalid inquiry_id'

    return jsonify({'message': message})


@app.route('/accept_order/<int:order_id>')
def accept_order(order_id):
    # UC-049 przyjmij zamowienie s.95
    if order_id > 0:
        message = 'Accepting order ' + str(order_id)
    else:
        message = 'Invalid order_id'

    return jsonify({'message': message})


@app.route('/get_inquiries')
def get_inquiries():
    # UC-050 pokaz liste zapytan ofertowych s.95
    return jsonify({'inquiries': inquiries})


@app.route('/submit_offer_to_client/<int:client_id>')
def submit_offer_to_client(client_id):
    # UC-051 zloz oferte klientowi s.95
    if client_id > 0:
        message = 'Submitting offer to client ' + str(client_id)
    else:
        message = 'Invalid client_id'

    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True)
