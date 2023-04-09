import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Publisher, Book, Sale, Shop, Stock

login = 'postgres'
password = '2209fynjy'
db_name = 'books_db'

DSN = f"postgresql://{login}:{password}@localhost:5432/{db_name}"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher_name = str(input("Введите имя автора: "))

q = session.query(Sale).join(Stock).join(Book).join(Publisher).filter(Publisher.name == publisher_name).all()
for s in q:
    print(f'{s.stock.book.title} | {s.stock.shop.name} | {s.price} | {s.date_sale}')

session.close()