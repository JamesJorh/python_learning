# VSCode Python调试入门示例
# 这是一个简单的入门示例，帮助您快速开始使用VSCode调试Python代码

def calculate_sum(a, b):
    """计算两个数的和"""
    # 调试提示: 在这里设置断点，观察参数a和b的值
    result = a + b
    return result

def calculate_product(a, b):
    """计算两个数的乘积"""
    # 调试提示: 在这里设置断点，观察参数a和b的值
    result = a * b
    return result

def main():
    print("===== VSCode Python调试入门 =====")
    print("欢迎使用VSCode调试Python代码！")
    print("请按照以下步骤开始调试:")
    print("1. 在左侧代码行号旁边点击设置断点(红点)")
    print("2. 按F5开始调试")
    print("3. 使用F10(单步跳过)或F11(单步进入)逐行执行代码")
    print("4. 观察变量窗口中的值变化")
    print("\n现在，让我们开始一个简单的计算:")
    
    # 输入值
    first_number = 10
    second_number = 5
    
    # 调试提示: 在下面几行设置断点，然后按F5开始调试