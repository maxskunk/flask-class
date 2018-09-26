from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, _id, name, price):
        self.id = _id
        self.name = name
        self.price = price

    @classmethod
    def find_by_name(cls, name):
        # Select * FROM items WHERE name = name
        return cls.query.filter_by(name=name).first()

    def insave_to_db(self):  # upserting
        db.session.add(self)
        db.session.commit()  # Updates and Inserts

    def upddelete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'name': self.name, 'price': self.price}
