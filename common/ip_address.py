import ipaddress
from fastapi import Request
import requests
from user_agents import parse


class IpAddress:
    """
    IP地址处理类
    """

    def __init__(self, ip: str, request: Request):
        self._ipaddress = ip
        self._request = request
        self._user_agent = parse(request.headers.get("User-Agent", ""))

        # 设置属性
        self._location = "内网" if self.is_internal_ip(
            ip) else self.external_ip_lookup(ip)
        self._browser = self._user_agent.get_browser()
        self._os = self._user_agent.get_os()

    @staticmethod
    def is_internal_ip(ip: str) -> bool:
        """
        检查是否为内网地址
        """

        try:
            ip_address = ipaddress.ip_address(ip)
            return ip_address.is_loopback or ip_address.is_private
        except ValueError:
            return False

    def external_ip_lookup(self, ip: str) -> str | None:
        """
        根据外部服务获取IP位置信息
        """

        try:
            response = requests.get(
                "http://whois.pconline.com.cn/ipJson.jsp",
                params={"ip": ip, "json": "true"},
                timeout=5,
            )
            response.raise_for_status()
            return response.json().get("addr", "未知位置")
        except (requests.RequestException, ValueError) as e:
            return "获取失败"

    @property
    def ipaddress(self) -> str:
        """
        返回IP地址
        """

        return self._ipaddress

    @property
    def location(self) -> str:
        """
        返回地理位置
        """

        return self._location

    @property
    def browser(self) -> str:
        """
        返回浏览器信息
        """

        return self._browser

    @property
    def os(self) -> str:
        """
        返回操作系统信息
        """

        return self._os
