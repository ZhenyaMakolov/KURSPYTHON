import os
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import functions as f

db_ip = os.environ["db_ip"]
db_port = os.environ["db_port"]
db_name = os.environ["db_name"]
db_pwd = os.environ["db_pwd"]
db_user = os.environ["db_user"]
DSN = f"postgresql://{db_user}:{db_pwd}@{db_ip}:{db_port}/{db_name}"
engine = sq.create_engine(DSN)
f.create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

f.load_data(session)

session.commit()
while True:
    user_input = input("Enter publisher name or ID (or zero to exit): ")
    if user_input == "0":
        session.close()
        exit()
    elif user_input.isdecimal():
        my_records = f.get_by_id(session, int(user_input))
        f.output(my_records)
        # for id, name in my_records.:
        #     print(id, name)
    else:
        my_records = f.get_by_name(session, user_input)
        f.output(my_records)