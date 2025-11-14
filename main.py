
from db.db_conn import DefaultSession
from sqlalchemy import select, text

def main():
    print('hello world')
    with DefaultSession() as db:
        a = db.execute(text('select * from test_schema.test_table'))
        b = a.fetchall()
        print(b)

if __name__ == '__main__':
    main()
