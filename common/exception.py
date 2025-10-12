from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from framework.response import Response


class BaseAppException(Exception):
    """
    基础应用异常类
    """

    def __init__(self, *, code: int, msg: str):
        self.code = code
        self.msg = msg
        super().__init__(self.msg)


class ExceptionHandler:
    """
    异常处理器
    """

    @staticmethod
    async def base_app_exception_handler(
        request: Request, exc: BaseAppException
    ) -> JSONResponse:
        """
        异常处理方法
        """

        return Response.fail(code=exc.code, msg=exc.msg)


def register_exception(app: FastAPI):
    """
    注册异常处理器
    """

    app.add_exception_handler(
        BaseAppException,
        ExceptionHandler.base_app_exception_handler,
    )


class ValidationException(BaseAppException):
    """
    请求参数校验异常类
    """

    def __init__(self, msg: str):
        super().__init__(code=500, msg=msg)


class BusinessException(BaseAppException):
    """
    业务异常类
    """

    def __init__(self, msg: str):
        super().__init__(code=500, msg=msg)


class AuthException(BaseAppException):
    """
    认证异常类
    """

    def __init__(self, msg: str):
        super().__init__(code=401, msg=msg)


class PermissionException(BaseAppException):
    """
    权限异常类
    """

    def __init__(self, msg: str):
        super().__init__(code=403, msg=msg)
