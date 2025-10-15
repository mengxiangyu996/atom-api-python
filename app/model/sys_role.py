from datetime import datetime
from typing import List
from sqlmodel import SQLModel, Field, Relationship
from zoneinfo import ZoneInfo
from app.model.sys_user import SysUser
from app.model.sys_menu import SysMenu
from app.model.sys_dept import SysDept


class SysRole(SQLModel, table=True):
    """
    角色信息表
    """

    __tablename__ = "sys_role"

    role_id: int = Field(description="角色id", primary_key=True)
    role_name: str = Field(description="角色名称", default="")
    role_key: str = Field(description="角色权限字符串", default="")
    role_sort: int = Field(description="显示顺序", default=0)
    data_scope: str = Field(
        description="数据范围：1-全部数据权限；2-自定数据权限；3-本部门数据权限；4-本部门及以下数据权限", default="1")
    menu_check_strictly: int = Field(description="菜单树选择项是否关联显示", default=1)
    dept_check_strictly: int = Field(description="部门树选择项是否关联显示", default=1)
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

    # 表关联
    sys_users: List[SysUser] = Relationship(
        back_populates="sys_roles", link_model="SysUserRole")
    sys_menus: List[SysMenu] = Relationship(
        back_populates="sys_roles", link_model="SysRoleMenu")
    sys_depts: List[SysDept] = Relationship(
        back_populates="sys_roles", link_model="SysRoleDept")
