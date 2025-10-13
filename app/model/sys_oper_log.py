from datetime import datetime
from sqlmodel import SQLModel, Field
from zoneinfo import ZoneInfo


class SysOperLog(SQLModel, table=True):
    """
    操作日志记录
    """

    __tablename__ = "sys_oper_log"

    oper_id: int = Field(description="日志id", primary_key=True)
    title: str = Field(description="模块标题", default="")
    business_type: int = Field(
        description="业务类型：0-其它；1-新增；2-修改；3-删除", default=0)
    method: str = Field(description="方法名称", default="")
    request_method: str = Field(description="请求方式", default="")
    oper_name: str = Field(description="操作人员", default="")
    dept_name: str = Field(description="部门名称", default="")
    oper_url: str = Field(description="请求url", default="")
    oper_ip: str = Field(description="主机地址", default="")
    oper_location: str = Field(description="操作地点", default="")
    oper_param: str = Field(description="请求参数", default="")
    json_result: str = Field(description="返回参数", default="")
    status: str = Field(description="操作状态：0-正常；1-异常", default="0")
    error_msg: str = Field(description="错误消息", default="")
    oper_time: datetime = Field(
        description="操作时间", default_factory=lambda: datetime.now(ZoneInfo("Asia/Shanghai")))
    cost_time: int = Field(description="消耗时间", default=0)
