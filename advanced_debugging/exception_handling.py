# 异常处理调试示例
# 本示例演示如何在VSCode中调试异常和错误

def divide(a, b):
    """除法函数，可能引发除零异常"""
    # 调试提示: 在这里设置断点，观察b为0时的情况
    return a / b

def access_list_element(my_list, index):
    """访问列表元素，可能引发索引错误"""
    # 调试提示: 在这里设置断点，观察索引超出范围的情况
    return my_list[index]

def parse_int(text):
    """将文本解析为整数，可能引发值错误"""
    # 调试提示: 在这里设置断点，观察非数字文本的情况
    return int(text)

def read_file(filename):
    """读取文件内容，可能引发文件不存在错误"""
    # 调试提示: 在这里设置断点，观察文件不存在的情况
    with open(filename, 'r') as file:
        return file.read()

def example_try_except():
    """try-except块示例"""
    print("\n===== try-except块调试 =====")
    
    # 除零异常处理
    try:
        # 调试提示: 在这里设置断点，然后使用F10(单步跳过)观察异常如何被捕获
        result = divide(10, 0)
        print(f"结果: {result}")
    except ZeroDivisionError as e:
        # 调试提示: 在这里设置断点，观察异常对象e的内容
        print(f"捕获到除零异常: {e}")
    
    # 索引错误处理
    my_list = [1, 2, 3, 4, 5]
    try:
        # 调试提示: 在这里设置断点，观察异常如何被捕获
        value = access_list_element(my_list, 10)
        print(f"值: {value}")
    except IndexError as e:
        print(f"捕获到索引错误: {e}")