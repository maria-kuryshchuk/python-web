from datetime import datetime

from flask import render_template, flash, request, redirect, url_for
from flask_paginate import Pagination

from app.misc import db
from . import main
from .forms import ProductForm
from ..models import Product, Category


@main.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@main.route('/', methods=['GET'])
def index():
    return redirect(url_for('main.products', page=1))


@main.route('/products/')
def products(page=1):
    products = db.session.query(Product).order_by(Product.id.desc())

    total = products.count()
    per_page = 10

    page = int(request.args.get("page", 1))

    factor = page - 1

    ofset = factor * per_page

    shown_products = products.limit(per_page).offset(ofset)

    paging = Pagination(page=page, per_page=per_page, offset=ofset, total=total, record_name=products,
                        css_framework='foundation')

    return render_template('products.html', products=shown_products, page=page, offset=ofset, pagination=paging)


@main.route('/products/edit/<int:id>', methods=['GET', 'POST'])
def editProduct(id):
    form = ProductForm(csrf_enabled=False)

    my_product = db.session.query(Product).get(id)

    category_id = my_product.categoryid
    categories = [(c.id, c.categoryname) for c in db.session.query(Category).all()]
    mycategory_name = db.session.query(Category).get(category_id)
    my_category = (category_id, mycategory_name)

    if request.method == 'GET' and my_product is not None:
        categories = [(c.id, c.categoryname) for c in db.session.query(Category).all()]
        form.product_name.data = my_product.name
        form.available.data = my_product.available
        form.count_in_storage.data = my_product.count
        form.price.data = my_product.price
        form.description.data = my_product.description
        form.category.choices = categories
        form.category.default = my_category
        form.category.data = my_category[0]

    elif request.method == 'GET' and my_product is None:
        print("no saved product")
        form.category.choices = categories

    form.category.choices = categories

    if form.validate_on_submit():
        product_name = form.product_name.data
        available = form.available.data
        count_in_storage = form.count_in_storage.data
        price = form.price.data
        description = form.description.data
        category = form.category.data

        db.session.query(Product).filter_by(id=id).update({'name': product_name,
                                                           'available': available,
                                                           'count': count_in_storage,
                                                           'price': price,
                                                           'description': description,
                                                           'categoryid': category}
                                                          )

        db.session.commit()

        flash('The product details %s have been updated' % product_name, 'success')

    return render_template('product_edit.html', form=form)


@main.route('/product/create', methods=['GET', 'POST'])
def createProduct():
    form = ProductForm(csrf_enabled=False)
    categories = [(c.id, c.categoryname) for c in db.session.query(Category).all()]
    quest = (0, "Select Category")
    form.category.choices = categories
    form.category.default = quest

    if form.validate_on_submit():
        product_name = form.product_name.data
        available = form.available.data
        count_in_storage = form.count_in_storage.data
        price = form.price.data
        description = form.description.data
        category = form.category.data

        product = Product(
            name=product_name,
            categoryid=category,
            available=available,
            count=count_in_storage,
            price=price,
            description=description
        )
        db.session.add(product)
        db.session.commit()

        flash('The new product %s has been saved' % product_name, 'success')

    return render_template('product_create.html', form=form)
