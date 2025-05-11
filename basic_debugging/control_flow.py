# 控制流程调试示例
# 本示例演示如何在VSCode中调试条件语句和循环结构

def main():
    # 条件语句调试
    print("===== 条件语句调试 =====")
    user_input = 15  # 模拟用户输入
    
    # 调试提示: 在if语句前设置断点，观察条件判断过程
    if user_input > 10:
        print(f"{user_input} 大于 10")
    elif user_input == 10:
        print(f"{user_input} 等于 10")
    else:
        print(f"{user_input} 小于 10")
    
    # 嵌套条件语句
    # 调试提示: 尝试在这里设置断点，然后使用F10(单步跳过)和F11(单步进入)观察执行流程
    if user_input % 2 == 0:
        print(f"{user_input} 是偶数")
        if user_input % 4 == 0:
            print(f"{user_input} 可以被4整除")
        else:
            print(f"{user_input} 不可以被4整除")
    else:
        print(f"{user_input} 是奇数")
        if user_input % 3 == 0:
            print(f"{user_input} 可以被3整除")
        else:
            print(f"{user_input} 不可以被3整除")
    
    # 循环结构调试
    print("\n===== 循环结构调试 =====")
    
    # for循环调试
    # 调试提示: 在循环内部设置断点，使用F5继续执行，观察每次循环的变量变化
    print("For循环示例:")
    for i in range(1, 6):
        square = i ** 2
        cube = i ** 3
        print(f"数字: {i}, 平方: {square}, 立方: {cube}")
    
    # while循环调试
    # 调试提示: 在while循环内设置断点，观察条件变化和循环执行过程
    print("\nWhile循环示例:")
    counter = 5
    while counter > 0:
        print(f"倒计时: {counter}")
        counter -= 1
    print("循环结束!")