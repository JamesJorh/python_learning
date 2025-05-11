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
    
    def inner_function(param):
        inner_var = "内部变量"
        # 调试提示: 在这里设置断点，观察可以访问哪些变量
        result = f"{outer_var} - {inner_var} - {param}"
        return result
    
    # 调试提示: 在这里设置断点，然后使用Step Into (F11)进入内部函数
    return inner_function("参数值")

def function_with_default_args(a, b=10, c="默认值"):
    """带默认参数的函数"""
    # 调试提示: 观察不同调用方式下参数的值
    return f"a={a}, b={b}, c={c}"

def main():
    # 基本函数调用
    print("===== 基本函数调用 =====")
    numbers = [5, 10, 15, 20, 25]
    print(f"数字列表: {numbers}")
    print(f"总和: {calculate_sum(numbers)}")
    print(f"平均值: {calculate_average(numbers)}")
    print(f"最大值: {find_max(numbers)}")
    
    # 函数返回值处理
    print("\n===== 函数返回值处理 =====")
    result = process_data(numbers)
    # 调试提示: 在这里设置断点，检查返回的字典内容
    print(f"处理结果: {result}")
    
    # 递归函数调用
    print("\n===== 递归函数调用 =====")
    n = 5
    # 调试提示: 使用F11(单步进入)观察递归调用过程
    factorial_result = recursive_factorial(n)
    print(f"{n}的阶乘是: {factorial_result}")
    
    # 嵌套函数和闭包
    print("\n===== 嵌套函数和闭包 =====")
    nested_result = nested_function_demo()
    print(f"嵌套函数结果: {nested_result}")
    
    # 默认参数演示
    print("\n===== 默认参数演示 =====")
    # 调试提示: 观察不同调用方式下参数的值
    print(function_with_default_args(1))
    print(function_with_default_args(1, 20))
    print(function_with_default_args(1, 20, "自定义值"))
    print(function_with_default_args(a=5, c="只设置a和c"))

if __name__ == "__main__":
    # 调试提示: 使用F11(单步进入)和Shift+F11(单步跳出)在函数之间导航
    main()
    print("程序执行完毕，尝试使用F11(单步进入)和Shift+F11(单步跳出)来调试函数调用。")