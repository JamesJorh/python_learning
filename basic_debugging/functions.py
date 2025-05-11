# 函数调用和堆栈跟踪示例
# 本示例演示如何在VSCode中调试函数调用、参数传递和返回值

def calculate_sum(numbers):
    """计算数字列表的总和"""
    # 调试提示: 在这里设置断点，观察传入的参数
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    """计算数字列表的平均值"""
    # 调试提示: 在这里设置断点，观察函数调用堆栈
    if not numbers:
        return 0
    total = calculate_sum(numbers)  # 调用另一个函数
    return total / len(numbers)

def find_max(numbers):
    """查找列表中的最大值"""
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def process_data(data_list):
    """处理数据并返回统计结果"""
    # 调试提示: 在这里设置断点，然后使用Step Into (F11)进入被调用的函数
    result = {
        "sum": calculate_sum(data_list),
        "average": calculate_average(data_list),
        "max": find_max(data_list),
        "length": len(data_list)
    }
    return result

def recursive_factorial(n):
    """递归计算阶乘，用于演示调用堆栈"""
    # 调试提示: 在递归函数中设置断点，观察调用堆栈如何增长和收缩
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)

def nested_function_demo():
    """嵌套函数示例，用于演示局部函数和闭包"""
    outer_var = "外部变量"