from logging.config import fileConfig

from alembic import context

from db.db_conn import ENGINE
from models import Base
from settings import DB_SCHEMA

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    print('run it offline')
    url = config.get_main_option("sqlalchemy.url")
    context.is_offline_mode()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    print('run it online')
    connectable = ENGINE

    with connectable.connect() as connection:
        # connection.execute(text(f'create schema if not exists {DB_SCHEMA}'))
        # connection.execute(text(f'set search_path to {DB_SCHEMA}'))

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            compare_type=True,
            version_table_schema=DB_SCHEMA
        )

        with context.begin_transaction():
            context.run_migrations()
        connection.commit()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
