from flask_wtf import Form
from wtforms import StringField, BooleanField, IntegerField, FloatField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class ProductForm(Form):
    product_name = StringField('name', validators = [DataRequired()])
    category = SelectField('category')
    available = BooleanField('available', default = False)
    count_in_storage = IntegerField('count in storage', validators = [DataRequired()])
    price = FloatField('price', validators = [DataRequired()])
    description = TextAreaField('description', default="")
