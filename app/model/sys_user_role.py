from sqlmodel import SQLModel, Field


class SysUserRole(SQLModel, table=True):
    """
    用户和角色关联表
    """

    __tablename__ = "sys_user_role"

    user_id: int = Field(description="用户id", foreign_key="sys_user.user_id")
    role_id: int = Field(description="角色id", foreign_key="sys_role.role_id")
