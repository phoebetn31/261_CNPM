from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from SaleApp import app, db

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=True, unique=True)
    products = relationship("Product", backref="category", lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=True, unique=True)
    price = Column(Float, default=0.0)
    image = Column(String(300), default="https://product.hstatic.net/1000300544/product/download__4__7d57157e7100431db9280bb4766a31ec.jpeg")
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=True)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        #c1 = Category(name="Mobile")
        #c2 = Category(name="Laptop")
        #db.session.add_all([c1,c2])
        #db.session.commit()

        #print(c1)

