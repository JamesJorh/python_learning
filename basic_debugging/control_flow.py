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
    
    # break和continue语句
    # 调试提示: 设置断点观察break和continue如何改变执行流程
    print("\nBreak和Continue示例:")
    for i in range(1, 10):
        if i == 3:
            print(f"遇到{i}，使用continue跳过")
            continue
        if i == 7:
            print(f"遇到{i}，使用break退出循环")
            break
        print(f"处理数字: {i}")
    
    # 综合示例: 猜数字游戏
    print("\n===== 猜数字游戏调试示例 =====")
    target_number = 42
    guess_count = 0
    max_guesses = 5
    
    # 调试提示: 尝试在循环内设置断点，观察不同猜测值的执行路径
    while guess_count < max_guesses:
        # 在实际应用中，这里会使用input()获取用户输入
        # 为了便于调试，我们使用预设的猜测值
        guesses = [30, 50, 40, 45, 42]  # 模拟用户的猜测序列
        guess = guesses[guess_count]
        
        guess_count += 1
        print(f"猜测 #{guess_count}: {guess}")
        
        if guess < target_number:
            print("太小了!")
        elif guess > target_number:
            print("太大了!")
        else:
            print(f"恭喜! 你用了 {guess_count} 次猜对了数字 {target_number}!")
            break
    
    if guess != target_number:
        print(f"游戏结束! 正确的数字是 {target_number}")

if __name__ == "__main__":
    # 调试提示: 使用不同的调试命令(F5, F9, F10, F11)来跟踪程序的执行流程
    main()
    print("程序执行完毕，尝试使用不同的断点位置来观察控制流程的变化。")