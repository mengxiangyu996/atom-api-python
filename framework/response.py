from typing import Any, TypeVar, Generic
from fastapi.responses import JSONResponse
from pydantic import BaseModel, model_serializer

T = TypeVar("T", bound=dict[str, Any] | list[Any] | BaseModel | Any)


class Response(BaseModel, Generic[T]):
    """
    FastAPI 标准化响应封装类

    提供统一的响应格式，包含状态码、消息和可选数据字段
    支持链式调用和泛型数据类型

    Attributes:
        status_code (int): HTTP状态码，默认200
        code (int): 业务状态码，默认10200(成功)
        msg (str): 消息描述，默认"成功"
        data (T | None): 响应数据，支持任意类型，默认为None
    """

    status_code: int = 200
    code: int = 10200
    msg: str = "成功"
    data: T | None = None

    @model_serializer
    def _serialize(self) -> dict:
        """内部序列化方法

        将模型转换为字典格式，自动处理Pydantic模型的序列化
        当data为None时不包含data字段

        Returns:
            序列化后的字典
        """

        result = {"code": self.code, "msg": self.msg}
        if self.data is not None:
            result["data"] = (
                self.data.model_dump()
                if isinstance(self.data, BaseModel)
                else self.data
            )
        return result

    def to_response(self, status_code: int | None, **kwargs) -> JSONResponse:
        """转换为FastAPI JSON响应

        Args:
            status_code: HTTP状态码，默认200
            **kwargs: 传递给JSONResponse的额外参数

        Returns:
            构造好的JSONResponse对象
        """

        http_statsu_code = status_code if status_code is not None else self.status_code
        return JSONResponse(
            status_code=http_statsu_code, content=self.model_dump(), **kwargs
        )

    @classmethod
    def success(
        cls, *, status_code: int = 200, code: int = 10200, msg: str = "成功", data: T | None = None
    ) -> "Response[T]":
        """创建成功响应

        Args:
            code: 业务状态码，默认200
            msg: 成功消息，默认"成功"
            data: 可选的成功数据

        Returns:
            构造好的成功响应实例
        """

        return cls(status_code=status_code, code=code, msg=msg, data=data).to_response(status_code)

    @classmethod
    def fail(
        cls, *, status_code: int = 200, code: int = 10500, msg: str = "失败", data: T | None = None
    ) -> "Response[T]":
        """创建失败响应

        Args:
            code: 业务状态码，默认10500
            msg: 错误消息，默认"失败"
            data: 可选的错误数据

        Returns:
            构造好的失败响应实例
        """

        return cls(status_code=status_code, code=code, msg=msg, data=data).to_response(status_code)

    @classmethod
    def page(cls, *, status_code: int = 200, code: int = 10200, rows: list[T], total: int) -> "Response[T]":
        """创建分页响应

        Args:
            items: 当前页数据列表
            total: 总记录数

        Returns:
            包含分页结构(data.items/data.total)的响应实例
        """

        return cls(status_code=status_code, code=code, data={"rows": rows, "total": total}).to_response(status_code)
