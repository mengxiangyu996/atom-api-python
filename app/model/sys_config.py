from datetime import datetime
from sqlmodel import SQLModel, Field
from zoneinfo import ZoneInfo


class SysConfig(SQLModel, table=True):
    """
    参数配置表
    """

    __tablename__ = "sys_config"

    config_id: int = Field(description="参数id", primary_key=True)
    config_name: str = Field(description="参数名称", max_length=100)
    config_key: str = Field(description="参数键名", max_length=100)
    config_value: str = Field(description="参数键值", max_length=500)
    config_type: str = Field(description="系统内置：Y-是；N-否", max_length=1)
    create_by: str = Field(description="创建者", max_length=64)
    create_time: datetime = Field(
        description="创建时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    update_by: str = Field(description="更新者", max_length=64)
    update_time: datetime = Field(
        description="更新时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    remark: str = Field(description="备注", max_length=500)
