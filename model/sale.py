from dataclasses import dataclass
from model.product import Product
from model.retailer import Retailer

from database.products_dao import ProductsDao
from database.retailers_dao import RetailersDao

import datetime

@dataclass
class Sale:
    date: datetime.date
    quantity: int
    unit_price: float
    unit_sale_price: float

    retailer_code: int
    product_number: int
    order_method_code: int
    retailer: Retailer = None
    product: Product = None
    product_brand = None

    def __post_init__(self):
        self.ricavo = self.quantity*self.unit_sale_price

    def __str__(self):
        return f"Data: {self.date}; Ricavo: {self.ricavo}; Retailer: {self.retailer_code}; Prodotto: {self.product_number}"

    def __eq__(self, other):
        return (self.retailer_code == other.retailer_code and
                self.product_number == other.product_number and
                self.order_method_code == other.order_method_code)

    def __hash__(self):
        return hash((self.retailer_code, self.product_number, self.order_method_code))

    def __lt__(self, other):
        return self.ricavo<other.ricavo

