import bcrypt
import jwt
from config.config import config
from common import exception
from datetime import datetime
from zoneinfo import ZoneInfo


class Security:
    """
    安全&认证&密码
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        生成哈希密码
        """

        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """
        验证密码
        """

        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

    @staticmethod
    def generate_token(current_user) -> str:
        """
        生成jwt令牌

        Args:
            current_user: 当前登录用户

        Returns:
            str: jwt令牌字符串

        Raises:
            Exception: 如果令牌生成失败
        """

        now: datetime = datetime.now(ZoneInfo("Asia/Shanghai"))

        payload: dict[str, int | str | datetime] = {
            "user": current_user,
            "exp": int(now.timestamp() + 86400),  # 过期时间
            "iat": int(now.timestamp()),  # 签发时间
            "iss": config.ruoyi.name,  # 签发者
        }

        try:
            return jwt.encode(
                payload=payload, key=config.token.secret, algorithm="HS256"
            )
        except Exception as e:
            raise Exception(f"Failed generate token: {str(e)}")

    @staticmethod
    def decode_token(token: str):
        """
        解码jwt令牌，返回其中的负载信息

        Args:
            token (str): jwt令牌字符串

        Returns:
            Dict[str, Any]: 解码后的payload

        Raises:
            ExpiredSignatureError: 令牌已过期
            InvalidIssuerError: 无效的签发者
            InvalidTokenError: 无效的令牌
            Exception: 其他解码错误
        """

        try:
            return jwt.decode(
                jwt=token, key=config.token.secret, algorithms=["HS256"]
            )
        except Exception as e:
            raise exception.AuthException(f"Failed decode token: {str(e)}")
