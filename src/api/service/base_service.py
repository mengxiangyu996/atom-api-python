from typing import TypeVar, Generic
import dal
from sqlmodel import SQLModel


T = TypeVar("T", bound=SQLModel)


class BaseService(Generic[T]):
    """
    基础服务类
    """

    def __init__(self, model: type[T]):
        self.model = model
        self.db = dal.db

    def get_by_id(self, item_id: int) -> T | None:
        with self.db.session() as session:
            session.get(self.model, item_id)
