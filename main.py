
from db.db_conn import DefaultSession
from sqlalchemy import text

from logger.setup_logger import setup_logger

from db.migrations import AlembicMigration

def main():
    logger = setup_logger()
    logger.info('hello world')
    with DefaultSession() as db:
        a = db.execute(text('select * from alembic_test_schema.test_alembic'))
        b = a.fetchall()

if __name__ == '__main__':
    main()
    ale = AlembicMigration()
    ale.create_revision('add comments', autogenerate=True)
    # ale.run_upgrade_db()
    # ale.run_downgrade_db('93b679cc1542')
