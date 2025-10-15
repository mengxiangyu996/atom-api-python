from pydantic import BaseModel
from config.config import config


class RedisKey(BaseModel):
    """
    缓存前缀
    """

    # 验证码 redis key
    captcha_code_key: str

    # 登录账户密码错误次数 redis key
    login_password_error_key: str

    # 登录用户 redis key
    user_token_key: str

    # 防重提交 redis key
    repeat_submit_key: str

    # 配置表数据 redis key
    sys_config_key: str

    # 字典表数据 redis key
    sys_dict_key: str

    class Config:
        allow_mutation = False

    @classmethod
    def create_keys(cls, config):
        return cls(
            captcha_code_key=f"{config.ruoyi.name}:captcha:code:",
            login_password_error_key=f"{config.ruoyi.name}:login:password:error:",
            user_token_key=f"{config.ruoyi.name}:user:token:",
            repeat_submit_key=f"{config.ruoyi.name}:repeat:submit:",
            sys_config_key=f"{config.ruoyi.name_PREFIX}:system:config",
            sys_dict_key=f"{config.ruoyi.name}:system:dict:data"
        )


# 创建 RedisKey 实例
redis_key = RedisKey.create_keys(config)


class BusinessType(BaseModel):
    """
    业务类型
    """

    request_business_type_other = 0  # 其他
    request_business_type_insert = 1  # 新增
    request_business_type_update = 2  # 修改
    request_business_type_delete = 3  # 删除
    request_business_type_grant = 4  # 授权
    request_business_type_export = 5  # 导出
    request_business_type_import = 6  # 导入
    request_business_type_force = 7  # 强退
    request_business_type_gencod = 8  # 生成代码
    request_business_type_clean = 9  # 清空数据

    class Config:
        allow_mutation = False
