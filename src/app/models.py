from app import db


class Product(db.Model):
    __tablename__ = 'Product'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(500))
    price_per_unit = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    unit = db.Column(db.String)

    def __init__(self, title, description, price_per_unit, quantity, unit):
        self.title = title
        self.description = description
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.unit = unit

    def __repr__(self):
        return '<Product %r>' % self.title
