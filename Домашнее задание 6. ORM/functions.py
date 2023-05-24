import json
import models as m

def create_tables(engine):
    m.Base.metadata.drop_all(engine)
    m.Base.metadata.create_all(engine)


def load_data(my_session):
    with open("fixtures\\tests_data.json", "r", encoding="utf-8") as initial_data:
        test_data = json.load(initial_data)

    for element in test_data:
        if element["model"] == "publisher":
            my_record = m.Publisher(
                id_publisher=element["pk"], name=element["fields"]["name"]
            )
            my_session.add(my_record)
        elif element["model"] == "book":
            my_record = m.Book(
                id_book=element["pk"],
                title=element["fields"]["title"],
                id_publisher=element["fields"]["id_publisher"],
            )
            my_session.add(my_record)
        elif element["model"] == "shop":
            my_record = m.Shop(id_shop=element["pk"], name=element["fields"]["name"])
            my_session.add(my_record)
        elif element["model"] == "stock":
            my_record = m.Stock(
                id_stock=element["pk"],
                id_book=element["fields"]["id_book"],
                id_shop=element["fields"]["id_shop"],
                count=element["fields"]["count"],
            )
            my_session.add(my_record)
        elif element["model"] == "sale":
            my_record = m.Sale(
                id_sale=element["pk"],
                price=element["fields"]["price"],
                date_sale=element["fields"]["date_sale"],
                count=element["fields"]["count"],
                id_stock=element["fields"]["id_stock"],
            )
            my_session.add(my_record)


def get_by_id(my_session, p_id):
    my_query = my_session.query(
        m.Publisher.name, m.Book.title, m.Sale.price, m.Sale.date_sale, m.Shop.name, m.Sale.count
    ).filter_by(id_publisher=p_id)
    my_query = my_query.join(m.Book, m.Book.id_publisher == m.Publisher.id_publisher)
    my_query = my_query.join(m.Stock, m.Stock.id_book == m.Book.id_book)
    my_query = my_query.join(m.Shop, m.Shop.id_shop == m.Stock.id_shop)
    my_query = my_query.join(m.Sale, m.Sale.id_stock == m.Stock.id_stock)
    my_records_ = my_query.all()
    return my_records_


def get_by_name(my_session, p_name):
    my_query = my_session.query(
        m.Publisher.name, m.Book.title, m.Sale.price, m.Sale.date_sale, m.Shop.name, m.Sale.count
    ).filter_by(name=p_name)
    my_query = my_query.join(m.Book, m.Book.id_publisher == m.Publisher.id_publisher)
    my_query = my_query.join(m.Stock, m.Stock.id_book == m.Book.id_book)
    my_query = my_query.join(m.Shop, m.Shop.id_shop == m.Stock.id_shop)
    my_query = my_query.join(m.Sale, m.Sale.id_stock == m.Stock.id_stock)
    my_records_ = my_query.all()
    return my_records_


def output(my_records_):
    for element in my_records_:
        print(f"{element[1]} | {element[4]} | {round(element[2] * element[5], 2)} | {element[3].date()}")