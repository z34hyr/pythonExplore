
from db.db_conn import DefaultSession
from sqlalchemy import text

from db.migrations import AlembicMigration

def main():
    print('hello world')
    with DefaultSession() as db:
        a = db.execute(text('select * from test_schema.test_table'))
        b = a.fetchall()
        print(b)

if __name__ == '__main__':
    ale = AlembicMigration()
    # ale.create_revision('add comments', autogenerate=True)
    ale.run_upgrade_db()
    # ale.run_downgrade_db('93b679cc1542')
