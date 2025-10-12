from datetime import datetime
from tortoise import Model, fields


class SysConfig(Model):
    """
    参数配置表
    """

    config_id: int = fields.BigIntField(
        description="参数id", primary_key=True, generated=True)
    config_name: str = fields.CharField(description="参数名称", max_length=100)
    config_key: str = fields.CharField(description="参数键名", max_length=100)
    config_value: str = fields.CharField(description="参数键值", max_length=500)
    config_type: str = fields.CharField(
        description="系统内置：Y-是；N-否", max_length=1)
    create_by: str = fields.CharField(description="创建者", max_length=64)
    create_time: datetime = fields.DatetimeField(
        description="创建时间", auto_now_add=True)
    update_by: str = fields.CharField(description="更新者", max_length=64)
    update_time: datetime = fields.DatetimeField(
        description="更新时间", auto_now=True)
    remark: str = fields.CharField(description="备注", max_length=500)

    class Meta:
        table = "sys_config"
        ordering = ["config_id"]
