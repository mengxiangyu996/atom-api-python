from sqlmodel import SQLModel, Field


class SysRoleDept(SQLModel, table=True):
    """
    角色和部门关联表
    """

    __tablename__ = "sys_role_dept"

    role_id: int = Field(description="角色id", foreign_key="sys_role.role_id")
    dept_id: int = Field(description="部门id", foreign_key="sys_dept.dept_id")
