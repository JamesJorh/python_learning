# API客户端调试示例
# 本示例演示如何在VSCode中调试API客户端应用

import requests
import json
import time
from urllib.parse import urljoin

# 模拟API基础URL
BASE_URL = "https://jsonplaceholder.typicode.com"

class APIClient:
    """API客户端类"""
    
    def __init__(self, base_url, timeout=10):
        """初始化API客户端
        
        Args:
            base_url: API基础URL
            timeout: 请求超时时间(秒)
        """
        # 调试提示: 在这里设置断点，观察初始化过程和参数
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "VSCode-Debug-Demo/1.0"
        })
    
    def get(self, endpoint, params=None):
        """发送GET请求
        
        Args:
            endpoint: API端点
            params: 查询参数
            
        Returns:
            响应对象
        """
        # 调试提示: 在这里设置断点，观察请求参数和URL构建
        url = urljoin(self.base_url, endpoint)
        print(f"发送GET请求: {url}")
        
        try:
            # 调试提示: 在这里设置断点，观察请求发送过程
            response = self.session.get(url, params=params, timeout=self.timeout)
            # 调试提示: 在这里设置断点，观察响应状态和内容
            response.raise_for_status()  # 抛出HTTP错误
            return response
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return None