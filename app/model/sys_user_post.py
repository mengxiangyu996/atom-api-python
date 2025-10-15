from sqlmodel import SQLModel, Field


class SysUserRole(SQLModel, table=True):
    """
    用户与岗位关联表
    """

    __tablename__ = "sys_user_post"

    user_id: int = Field(description="用户id", foreign_key="sys_user.user_id")
    post_id: int = Field(description="岗位id", foreign_key="sys_post.post_id")
