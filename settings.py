import os

DEBUG = os.getenv('DEBUG', True)

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_SCHEMA = 'alembic_test_schema'

DATABASE = {
    'default': {
        'drivername': 'postgresql+psycopg2',
        'database': DB_NAME,
        'username': DB_USER,
        'password': DB_PASSWORD,
        'query': {
            'host': DB_HOST,
            'port': DB_PORT,
        }
    },
    'async': {
        'drivername': 'postgresql+asyncpg',
        'database': DB_NAME,
        'username': DB_USER,
        'password': DB_PASSWORD,
    }
}

SQLA_POOL_SIZE = 3

DB_ECHO = True
DB_POOL_ECHO = True

SQLA_ENGINE = {
    'pool_recycle': 60 * 10,
    'pool_pre_ping': True,
    'pool_size': SQLA_POOL_SIZE,
    'max_overflow': SQLA_POOL_SIZE,
    'pool_timeout': 30,
    'echo': DB_ECHO,
    'echo_pool': DB_POOL_ECHO,
}