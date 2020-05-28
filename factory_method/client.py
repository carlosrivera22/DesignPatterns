from factory import ProductFactory
from products import *

products = [ ProductFactory.createProduct("Product"),
             ProductFactory.createProduct("Product2")]

for product in products:
    product.execute()

