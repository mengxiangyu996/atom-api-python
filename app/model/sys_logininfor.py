from datetime import datetime
from sqlmodel import SQLModel, Field
from zoneinfo import ZoneInfo


class SysLogininfor(SQLModel, table=True):
    """
    系统访问记录
    """

    __tablename__ = "sys_logininfor"

    info_id: int = Field(description="访问id", primary_key=True)
    user_name: str = Field(description="用户账号", default="")
    ipaddr: str = Field(description="登陆地点", default="")
    browser: str = Field(description="浏览器类型", default="")
    os: str = Field(description="操作系统", default="")
    status: str = Field(description="状态：0-成功；1-失败", default="0")
    msg: str = Field(description="提示消息", default="")
    login_time: datetime = Field(
        description="访问时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
