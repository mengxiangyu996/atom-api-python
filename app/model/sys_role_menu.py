from sqlmodel import SQLModel, Field


class SysRoleMenu(SQLModel, table=True):
    """
    角色和菜单关联表
    """

    __tablename__ = "sys_role_menu"

    role_id: int = Field(description="角色id", foreign_key="sys_role.role_id")
    menu_id: int = Field(description="菜单id", foreign_key="sys_menu.menu_id")
