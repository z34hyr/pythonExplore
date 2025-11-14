import logging
import settings

from contextlib import contextmanager, asynccontextmanager

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from typing import ContextManager

LOGGER = logging.getLogger(__name__)

@contextmanager
def session_scope(session_builder, log=True, logger: logging.Logger = LOGGER):
    """Предоставление отдельных сессий для транзакций при выполнении действий с БД"""
    session: Session = session_builder()
    if log:
        logger.info("DB session `%s` is initialized!", session.hash_key)
    try:
        session.execute(text("set timezone = 'UTC'"))
        yield session
        session.commit()
    except Exception as e:
        if log:
            logger.exception(type(e).__name__)
        session.rollback()
        raise
    finally:
        session.close()
        if log:
            logger.info("DB session `%s` iis closed!", session.hash_key)


ENGINE = create_engine(URL.create(**settings.DATABASE['default']), **settings.SQLA_ENGINE)
SESSION = sessionmaker(ENGINE)
SCOPED_SESSION = scoped_session(SESSION)

@contextmanager
def default_session(*args, **kwargs) -> ContextManager[Session]:
    with session_scope(SESSION, *args, **kwargs) as db:
        yield db

@contextmanager
def default_scoped_session(*args, **kwargs) -> ContextManager[Session]:
    with session_scope(SCOPED_SESSION, *args, **kwargs) as db:
        yield db

DefaultSession = default_session
DefaultScopedSession = default_scoped_session
