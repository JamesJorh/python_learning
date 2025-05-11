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
            # 调试提示: 在这里设置断点，观察异常处理
            print(f"请求错误: {e}")
            return None
    
    def post(self, endpoint, data):
        """发送POST请求
        
        Args:
            endpoint: API端点
            data: 请求数据
            
        Returns:
            响应对象
        """
        # 调试提示: 在这里设置断点，观察请求数据
        url = urljoin(self.base_url, endpoint)
        print(f"发送POST请求: {url}")
        
        try:
            # 调试提示: 使用F11(单步进入)观察请求发送过程
            response = self.session.post(
                url, 
                data=json.dumps(data), 
                timeout=self.timeout
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return None
    
    def put(self, endpoint, data):
        """发送PUT请求"""
        url = urljoin(self.base_url, endpoint)
        print(f"发送PUT请求: {url}")
        
        try:
            response = self.session.put(
                url, 
                data=json.dumps(data), 
                timeout=self.timeout
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return None
    
    def delete(self, endpoint):
        """发送DELETE请求"""
        url = urljoin(self.base_url, endpoint)
        print(f"发送DELETE请求: {url}")
        
        try:
            response = self.session.delete(url, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return None

# 示例函数：获取用户列表
def get_users(api_client, limit=None):
    """获取用户列表
    
    Args:
        api_client: API客户端实例
        limit: 限制返回的用户数量
        
    Returns:
        用户列表或None
    """
    # 调试提示: 在这里设置断点，观察参数和查询构建
    params = {}
    if limit:
        params["_limit"] = limit
    
    # 调试提示: 使用F11(单步进入)进入get方法
    response = api_client.get("/users", params=params)
    
    if response:
        # 调试提示: 在这里设置断点，观察JSON解析过程
        try:
            users = response.json()
            return users
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
    
    return None

# 示例函数：获取单个用户
def get_user(api_client, user_id):
    """获取单个用户信息
    
    Args:
        api_client: API客户端实例
        user_id: 用户ID
        
    Returns:
        用户信息或None
    """
    # 调试提示: 观察URL构建过程
    endpoint = f"/users/{user_id}"
    
    response = api_client.get(endpoint)
    
    if response:
        try:
            user = response.json()
            return user
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
    
    return None

# 示例函数：创建用户
def create_user(api_client, user_data):
    """创建新用户
    
    Args:
        api_client: API客户端实例
        user_data: 用户数据
        
    Returns:
        创建的用户信息或None
    """
    # 调试提示: 在这里设置断点，观察请求数据
    response = api_client.post("/users", user_data)
    
    if response:
        try:
            created_user = response.json()
            return created_user
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
    
    return None

# 示例函数：更新用户
def update_user(api_client, user_id, user_data):
    """更新用户信息"""
    endpoint = f"/users/{user_id}"
    response = api_client.put(endpoint, user_data)
    
    if response:
        try:
            updated_user = response.json()
            return updated_user
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
    
    return None

# 示例函数：删除用户
def delete_user(api_client, user_id):
    """删除用户"""
    endpoint = f"/users/{user_id}"
    response = api_client.delete(endpoint)
    
    if response:
        return response.status_code == 200
    
    return False

# 示例函数：处理分页数据
def get_paginated_data(api_client, endpoint, page_size=10):
    """获取分页数据的示例
    
    Args:
        api_client: API客户端实例
        endpoint: API端点
        page_size: 每页数据量
        
    Returns:
        所有数据的列表
    """
    # 调试提示: 在这里设置断点，观察分页处理逻辑
    all_data = []
    page = 1
    more_data = True
    
    while more_data:
        # 调试提示: 在循环内设置断点，观察每次请求
        params = {
            "_page": page,
            "_limit": page_size
        }
        
        response = api_client.get(endpoint, params=params)
        
        if response and response.status_code == 200:
            try:
                data = response.json()
                if data:
                    all_data.extend(data)
                    page += 1
                    # 模拟请求间隔，避免频繁请求
                    time.sleep(0.5)
                else:
                    more_data = False
            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")
                more_data = False
        else:
            more_data = False
    
    return all_data

# 示例函数：错误处理和重试
def get_with_retry(api_client, endpoint, max_retries=3, retry_delay=1):
    """带重试机制的GET请求
    
    Args:
        api_client: API客户端实例
        endpoint: API端点
        max_retries: 最大重试次数
        retry_delay: 重试间隔(秒)
        
    Returns:
        响应数据或None
    """
    # 调试提示: 在这里设置断点，观察重试逻辑
    retries = 0
    
    while retries < max_retries:
        # 调试提示: 在循环内设置断点，观察每次重试
        response = api_client.get(endpoint)
        
        if response and response.status_code == 200:
            try:
                return response.json()
            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")
                return None
        
        retries += 1
        if retries < max_retries:
            print(f"请求失败，{retry_delay}秒后重试({retries}/{max_retries})...")
            time.sleep(retry_delay)
    
    print(f"达到最大重试次数({max_retries})，请求失败")
    return None

def main():
    print("===== API客户端调试示例 =====")
    print("本示例演示如何调试API客户端应用")
    print(f"使用的API: {BASE_URL}\n")
    
    # 创建API客户端
    # 调试提示: 在这里设置断点，观察客户端初始化
    api_client = APIClient(BASE_URL)
    
    # 获取用户列表
    print("\n获取用户列表(限制5个)...")
    # 调试提示: 使用F11(单步进入)进入get_users函数
    users = get_users(api_client, limit=5)
    if users:
        print(f"获取到 {len(users)} 个用户")
        for user in users:
            print(f"  - {user['id']}: {user['name']} ({user['email']})")
    
    # 获取单个用户
    print("\n获取单个用户(ID=1)...")
    # 调试提示: 使用F11(单步进入)进入get_user函数
    user = get_user(api_client, 1)
    if user:
        print(f"用户信息: {user['name']} ({user['email']})")
        print(f"地址: {user['address']['street']}, {user['address']['city']}")
        print(f"公司: {user['company']['name']}")
    
    # 创建用户
    print("\n创建新用户...")
    new_user_data = {
        "name": "张三",
        "username": "zhangsan",
        "email": "zhangsan@example.com",
        "address": {
            "street": "测试街道",
            "city": "北京",
            "zipcode": "100000"
        },
        "phone": "123-456-7890"
    }
    # 调试提示: 使用F11(单步进入)进入create_user函数
    created_user = create_user(api_client, new_user_data)
    if created_user:
        print(f"创建的用户ID: {created_user['id']}")
        print(f"用户信息: {created_user}")
    
    # 更新用户
    print("\n更新用户(ID=1)...")
    update_data = {
        "name": "更新的名字",
        "email": "updated@example.com"
    }
    updated_user = update_user(api_client, 1, update_data)
    if updated_user:
        print(f"更新后的用户信息: {updated_user}")
    
    # 删除用户
    print("\n删除用户(ID=1)...")
    deleted = delete_user(api_client, 1)
    print(f"删除结果: {'成功' if deleted else '失败'}")
    
    # 分页获取数据
    print("\n分页获取帖子数据...")
    # 调试提示: 使用F11(单步进入)进入get_paginated_data函数
    posts = get_paginated_data(api_client, "/posts", page_size=10)
    print(f"获取到 {len(posts)} 个帖子")
    
    # 带重试的请求
    print("\n带重试机制的请求(模拟)...")
    # 这里我们请求一个不存在的端点来模拟失败
    # 调试提示: 使用F11(单步进入)进入get_with_retry函数
    result = get_with_retry(api_client, "/non-existent", max_retries=3, retry_delay=1)
    print(f"请求结果: {result}")

if __name__ == "__main__":
    # 调试提示: 按F5开始调试，使用断点观察API请求和响应处理
    main()
    print("\n程序执行完毕，尝试在不同的API调用阶段设置断点并观察执行流程。")
    print("API客户端调试是Web开发中常见的场景，掌握它将帮助您更好地开发和调试网络应用。")