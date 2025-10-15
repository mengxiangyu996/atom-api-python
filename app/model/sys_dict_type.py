from datetime import datetime
from typing import List
from sqlmodel import SQLModel, Field, Relationship
from zoneinfo import ZoneInfo
from app.model.sys_dict_data import SysDictData


class SysDictType(SQLModel, table=True):
    """
    字典类型表
    """

    __tablename__ = "sys_dict_type"

    dict_id: int = Field(description="字典id", primary_key=True)
    dict_name: str = Field(description="字典名称", default="")
    dict_type: str = Field(description="字典类型", default="")
    status: str = Field(description="状态：0-正常；1-停用", default="0")
    create_by: str = Field(description="创建者", default="")
    create_time: datetime = Field(
        description="创建时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    update_by: str = Field(description="更新者", default="")
    update_time: datetime = Field(
        description="更新时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    remark: str = Field(description="备注", default=None)

    # 表关联
    sys_dict_data: List[SysDictData] = Relationship(
        back_populates="sys_dict_type")
