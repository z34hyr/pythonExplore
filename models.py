
from sqlalchemy import (
    MetaData, Text, Integer, )
from sqlalchemy.orm import declarative_base, mapped_column

from settings import DB_SCHEMA

schema = DB_SCHEMA

meta = MetaData(schema=schema)
Base = declarative_base(metadata=meta)

class TestAlembic(Base):
    __tablename__ = 'test_alembic'

    id = mapped_column(Integer, primary_key=True, comment='ID записи')
    name = mapped_column(Text, nullable=True, default=None, comment='Техническое имя колонки')
    display_name = mapped_column(Text, nullable=True, default=None, comment='Человекочитаемое имя колонки')
