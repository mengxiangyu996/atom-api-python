import re


class Regex:
    """
    正则表达式
    """

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        检查手机号是否合法
        """

        return re.match(re.compile(r"1[356789]\d{9}"), phone) is not None

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        检查邮箱地址是否合法
        """

        return (
            re.match(
                re.compile(
                    r"[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)"), email
            )
            is not None
        )

    @staticmethod
    def validate_idcard(idcard: str) -> bool:
        """
        检查身份证号是否合法
        """

        return (
            re.match(
                re.compile(
                    r"[1-9]\d{5}(?:18|19|(?:[23]\d))\d{2}(?:(?:0[1-9])|(?:10|11|12))(?:(?:[0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]"
                ),
                idcard,
            )
            is not None
        )
