from app import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(55), index=True)
    available = db.Column(db.Boolean())
    count = db.Column(db.Integer())
    price = db.Column(db.Float())
    description = db.Column(db.Text())

    categoryid = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', backref='products')

    def __repr__(self):
        return '<product % r>' % self.name


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    categoryname = db.Column(db.String(40), unique=True)

    def __repr__(self):
        return '<category % r>' % self.categoryname
