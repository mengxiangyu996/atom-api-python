from datetime import datetime
from sqlmodel import SQLModel, Field
from zoneinfo import ZoneInfo


class SysDictData(SQLModel, table=True):
    """
    字典数据表
    """

    __tablename__ = "sys_dict_data"

    dict_code: int = Field(description="字典编码", primary_key=True)
    dict_sort: int = Field(description="字典排序", default=0)
    dict_label: str = Field(description="字典标签", default="")
    dict_value: str = Field(description="字典键值", default="")
    dict_type: str = Field(description="字典类型", default="")
    css_class: str = Field(description="样式属性（其他样式扩展）")
    list_class: str = Field(description="表格回显样式")
    is_default: str = Field(description="是否默认：Y-是；N-否", default="N")
    status: str = Field(description="状态：0-正常；1-停用", default="0")
    create_by: str = Field(description="创建者", default="")
    create_time: datetime = Field(
        description="创建时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    update_by: str = Field(description="更新者", default="")
    update_time: datetime = Field(
        description="更新时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    remark: str = Field(description="备注", default=None)
