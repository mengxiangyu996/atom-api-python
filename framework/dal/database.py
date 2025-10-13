from contextlib import contextmanager
from sqlmodel import Session, create_engine
from typing import Iterator
import threading


class _Database:

    def __init__(self, db_url: str):
        self._engine = create_engine(db_url, echo=True)
        self._lock = threading.Lock()

    @property
    def client(self):
        return self._engine

    @contextmanager
    def session(self) -> Iterator[Session]:
        """
        提供上下文管理的 Session
        """

        session = Session(self._engine, expire_on_commit=False)
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
