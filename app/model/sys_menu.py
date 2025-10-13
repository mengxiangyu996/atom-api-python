from datetime import datetime
from sqlmodel import SQLModel, Field
from zoneinfo import ZoneInfo


class SysMenu(SQLModel, table=True):
    """
    菜单权限表
    """

    __tablename__ = "sys_menu"

    menu_id: int = Field(description="菜单id", primary_key=True)
    menu_name: str = Field(description="菜单名称", default="")
    parent_id: int = Field(description="父菜单id", default=0)
    order_num: int = Field(description="显示顺序", default=0)
    path: str = Field(description="路由地址", default="")
    component: str = Field(description="组件路径", default="")
    query: str = Field(description="路由参数", default="")
    route_name: str = Field(description="路由名称", default="")
    is_frame: int = Field(description="是否为外链：0-是；1-否", default=1)
    is_cache: int = Field(description="是否缓存：0-缓存；1-不缓存", default=0)
    menu_type: str = Field(description="菜单类型：M-目录；C-菜单；F-按钮", default="")
    visible: str = Field(description="菜单状态：0-显示；1-隐藏", default="0")
    perms: str = Field(description="权限标识", default=None)
    icon: str = Field(description="菜单图标", default="#")
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
