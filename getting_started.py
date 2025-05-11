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
    sum_result = calculate_sum(first_number, second_number)
    print(f"{first_number} + {second_number} = {sum_result}")
    
    product_result = calculate_product(first_number, second_number)
    print(f"{first_number} × {second_number} = {product_result}")
    
    # 尝试修改变量值
    # 调试提示: 在这里设置断点，然后在调试时尝试修改变量值
    for i in range(1, 5):
        print(f"循环 {i}: {first_number} + {i} = {first_number + i}")
    
    print("\n恭喜！您已完成基本调试流程的学习。")
    print("接下来，您可以探索项目中的其他示例来学习更多调试技巧。")

if __name__ == "__main__":
    # 调试提示: 按F5开始调试，F9设置/取消断点
    main()
    print("\n程序执行完毕。尝试重新运行并使用不同的断点位置来熟悉调试过程。")