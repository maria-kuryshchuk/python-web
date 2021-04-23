from app.models import Category, Product
from sampledata import categories, products


class Seeder():

    def __init__(self, categories=categories, products=products):
        self.categories = categories
        self.products = products

    def _getCategories(self):
        return self.categories

    def _getProducts(self):
        return self.products

    def category_seed(self, db):
        categories = self._getCategories()

        for category in categories:
            print("adding %s into category table" % category)
            categoryname = category
            category = Category(categoryname=categoryname)
            db.session.add(category)

    def product_seed(self, db):
        products = self._getProducts()

        for product in products:
            print("adding %s into products table" % product)
            name = product[0]
            available = product[1]
            count = product[2]
            price = product[3]
            description = product[4]
            categoryid = product[5]

            product = Product(name=name,
                              available=available,
                              count=count,
                              price=price,
                              description=description,
                              categoryid=categoryid)
            db.session.add(product)
