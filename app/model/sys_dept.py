from datetime import datetime
from typing import List
from sqlmodel import SQLModel, Field, Relationship
from zoneinfo import ZoneInfo
from app.model.sys_user import SysUser
from app.model.sys_role import SysRole


class SysDept(SQLModel, table=True):
    """
    部门表
    """

    __tablename__ = "sys_dept"

    dept_id: int = Field(description="部门id", primary_key=True)
    parent_id: int = Field(description="父部门id", default=0)
    ancestors: str = Field(description="祖级列表", default="")
    dept_name: str = Field(description="部门名称", default="")
    order_num: int = Field(description="显示顺序", default=0)
    leader: str = Field(description="负责人", default=None)
    phone: str = Field(description="联系电话", default=None)
    email: str = Field(description="邮箱", default=None)
    status: str = Field(description="状态：0-正常；1-停用", default="0")
    create_by: str = Field(description="创建者", default="")
    create_time: datetime = Field(
        description="创建时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    update_by: str = Field(description="更新者", default="")
    update_time: datetime = Field(
        description="更新时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    delete_time: datetime = Field(description="删除时间", default=None)

    # 表关联
    sys_users: List[SysUser] = Relationship(back_populates="sys_dept")
    sys_roles: List[SysRole] = Relationship(
        back_populates="sys_depts", link_model="SysRoleDept")
