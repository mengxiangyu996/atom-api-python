from datetime import datetime
from sqlmodel import SQLModel, Field
from zoneinfo import ZoneInfo


class SysUser(SQLModel, table=True):
    """
    用户信息表
    """

    __tablename__ = "sys_user"

    user_id: int = Field(description="用户id", primary_key=True)
    dept_id: int = Field(description="部门id", default=0)
    user_name: str = Field(description="用户账号", default="")
    nick_name: str = Field(description="用户昵称", default="")
    user_type: str = Field(description="用户类型：00-系统用户", default="00")
    email: str = Field(description="用户邮箱", default="")
    phonenumber: str = Field(description="手机号码", default="")
    sex: str = Field(description="用户性别：0-男；1-女；2-未知", default="0")
    avatar: str = Field(description="头像地址", default="")
    password: str = Field(description="密码", default="")
    login_ip: str = Field(description="最后登录ip", default="")
    login_date: datetime = Field(description="最后登录时间", default=None)
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
