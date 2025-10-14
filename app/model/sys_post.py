from datetime import datetime
from sqlmodel import SQLModel, Field
from zoneinfo import ZoneInfo


class SysPost(SQLModel, table=True):
    """
    岗位信息表
    """

    __tablename__ = "sys_post"

    post_id: int = Field(description="岗位id", primary_key=True)
    post_code: str = Field(description="岗位编码", default="")
    post_name: str = Field(description="岗位名称", default="")
    post_sort: int = Field(description="显示顺序", default=0)
    status: str = Field(description="状态：0-正常；1-停用", default="0")
    create_by: str = Field(description="创建者", default="")
    create_time: datetime = Field(
        description="创建时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    update_by: str = Field(description="更新者", default="")
    update_time: datetime = Field(
        description="更新时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    delete_time: datetime = Field(
        description="删除时间", default=None)
    remark: str = Field(description="备注", default=None)
