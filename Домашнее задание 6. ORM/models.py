import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Sale(Base):
    __tablename__ = "sale"
    id_sale = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.DateTime(timezone=True), nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id_stock"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    stock = relationship("Stock", back_populates="sales")


class Stock(Base):
    __tablename__ = "stock"
    id_stock = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id_book"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id_shop"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    sales = relationship("Sale", back_populates="stock")
    book = relationship("Book", back_populates="stocks")
    shop = relationship("Shop", back_populates="stocks")


class Book(Base):
    __tablename__ = "book"
    id_book = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(100), nullable=False)
    id_publisher = sq.Column(
        sq.Integer, sq.ForeignKey("publisher.id_publisher"), nullable=False
    )
    stocks = relationship("Stock", back_populates="book")
    publisher = relationship("Publisher", back_populates="books")


class Shop(Base):
    __tablename__ = "shop"
    id_shop = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(50), nullable=False)
    stocks = relationship("Stock", back_populates="shop")


class Publisher(Base):
    __tablename__ = "publisher"
    id_publisher = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(50), nullable=False)
    books = relationship("Book", back_populates="publisher")