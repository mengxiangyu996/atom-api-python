from pydantic import BaseModel, Field, ConfigDict
from pydantic_yaml import parse_yaml_file_as


class RuoYiConfig(BaseModel):
    """
    项目相关配置
    """

    name: str = Field(description="名称")
    version: str = Field(description="版本")
    copyright: int = Field(description="版权年份")
    domain: str = Field(description="域名")
    ssl: bool = Field(description="启用SSL")
    upload_path: str = Field(description="文件上传路径", alias="uploadPath")

    model_config = ConfigDict(
        populate_by_name=True,  # 允许别名作为输入
        serialize_by_alias=True,  # 输出默认用别名
        from_attributes=True,  # 允许从 ORM 对象加载
    )


class ServerConfig(BaseModel):
    """
    开发环境配置
    """

    host: str = Field(description="地址")
    port: int = Field(description="端口")
    debug: bool = Field(description="开发环境")

    model_config = ConfigDict(
        populate_by_name=True,  # 允许别名作为输入
        serialize_by_alias=True,  # 输出默认用别名
        from_attributes=True,  # 允许从 ORM 对象加载
    )


class MysqlConfig(BaseModel):
    """
    数据库配置
    """

    host: str = Field(description="地址")
    port: int = Field(description="端口")
    database: str = Field(description="数据库名称")
    username: str = Field(description="用户名")
    password: str = Field(description="密码")
    charset: str = Field(description="编码")

    model_config = ConfigDict(
        populate_by_name=True,  # 允许别名作为输入
        serialize_by_alias=True,  # 输出默认用别名
        from_attributes=True,  # 允许从 ORM 对象加载
    )


class RedisConfig(BaseModel):
    """
    redis 配置
    """

    host: str = Field(description="地址")
    port: int = Field(description="端口")
    database: int = Field(description="数据库索引")
    password: str | None = Field(description="密码")

    model_config = ConfigDict(
        populate_by_name=True,  # 允许别名作为输入
        serialize_by_alias=True,  # 输出默认用别名
        from_attributes=True,  # 允许从 ORM 对象加载
    )


class TokenConfig(BaseModel):
    """
    token 配置
    """

    header: str = Field(description="令牌自定义标识")
    secret: str = Field(description="令牌密钥")
    expire_time: int = Field(description="令牌有效期", alias="expireTime")

    model_config = ConfigDict(
        populate_by_name=True,  # 允许别名作为输入
        serialize_by_alias=True,  # 输出默认用别名
        from_attributes=True,  # 允许从 ORM 对象加载
    )


class UserPasswordConfig(BaseModel):
    """
    用户密码配置
    """

    max_retry_count: int = Field(description="密码最大错误次数", alias="maxRetryCount")
    lock_time: int = Field(description="密码锁定时间", alias="lockTime")

    model_config = ConfigDict(
        populate_by_name=True,  # 允许别名作为输入
        serialize_by_alias=True,  # 输出默认用别名
        from_attributes=True,  # 允许从 ORM 对象加载
    )


class UserConfig(BaseModel):
    """
    用户配置
    """

    password: UserPasswordConfig = Field(description="用户密码配置")

    model_config = ConfigDict(
        populate_by_name=True,  # 允许别名作为输入
        serialize_by_alias=True,  # 输出默认用别名
        from_attributes=True,  # 允许从 ORM 对象加载
    )


class Config(BaseModel):
    """
    配置文件
    """

    ruoyi: RuoYiConfig = Field(description="项目相关配置")
    server: ServerConfig = Field(description="开发环境配置")
    mysql: MysqlConfig = Field(description="数据库配置")
    redis: RedisConfig = Field(description="redis配置")
    token: TokenConfig = Field(description="token配置")
    user: UserConfig = Field(description="用户配置")

    model_config = ConfigDict(
        populate_by_name=True,  # 允许别名作为输入
        serialize_by_alias=True,  # 输出默认用别名
        from_attributes=True,  # 允许从 ORM 对象加载
    )


config = parse_yaml_file_as(Config, "application.yaml")
