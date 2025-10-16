from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.response.response import Response


class BaseApiException(Exception):
    """
    基础应用异常类
    """

    def __init__(self, *, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(self.message)


class ExceptionHandler:
    """
    异常处理器
    """

    @staticmethod
    async def base_app_exception_handler(
        request: Request, exc: BaseApiException
    ) -> JSONResponse:
        """
        异常处理方法
        """

        return Response.fail(code=exc.code, message=exc.message)


def register_exception(app: FastAPI):
    """
    注册异常处理器
    """

    app.add_exception_handler(
        BaseApiException,
        ExceptionHandler.base_app_exception_handler,
    )


class ValidationException(BaseApiException):
    """
    请求参数校验异常类
    """

    def __init__(self, message: str):
        super().__init__(code=10500, message=message)


class BusinessException(BaseApiException):
    """
    业务异常类
    """

    def __init__(self, message: str):
        super().__init__(code=10500, message=message)


class AuthException(BaseApiException):
    """
    认证异常类
    """

    def __init__(self, message: str):
        super().__init__(code=10401, message=message)


class PermissionException(BaseApiException):
    """
    权限异常类
    """

    def __init__(self, message: str):
        super().__init__(code=10403, message=message)
