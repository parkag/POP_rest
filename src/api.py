from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


def get_products():
	# UC-008 przegladaj katalog s.37
	return 'Not implemented'


@app.route('add')
def add_product_to_inquiry():
	# UC-009 dodaj produkt do zapytania ofertowego s.37
	return 'Not implemented'


def remove_product_from_inquiry():
	# UC-011 usun produkt z zapytania ofertowego s.37
	return 'Not implemented'


def submit_inquiry():
	# UC-010 zloz zapytanie ofertowe s.37
	return 'Not implemented'


def accept_inquiry():
	# UC-048 przyjmij zapytanie ofertowe s.95
	return


def accept_order():
	# UC-049 przyjmij zamowienie s.95
	return


def get_inquiries():
	# UC-050 pokaz liste zapytan ofertowych s.95
	return


def make_an_offer_to_client():
	# UC-051 zloz oferte klientowi s.95
	return

if __name__ == '__main__':
    app.run(debug=True)
