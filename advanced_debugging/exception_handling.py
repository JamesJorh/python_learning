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

def example_multiple_except():
    """多个except块示例"""
    print("\n===== 多个except块调试 =====")
    
    # 调试提示: 在try块内设置断点，然后观察不同类型的异常如何被不同的except块捕获
    inputs = ["10", "abc", "0"]
    for input_text in inputs:
        try:
            # 这里可能发生多种异常
            number = parse_int(input_text)
            result = 100 / number
            print(f"结果: 100 / {number} = {result}")
        except ValueError as e:
            print(f"值错误: {e}")
        except ZeroDivisionError as e:
            print(f"除零错误: {e}")
        except Exception as e:
            print(f"其他错误: {e}")

def example_finally():
    """finally块示例"""
    print("\n===== finally块调试 =====")
    
    # 调试提示: 观察finally块如何在异常发生和未发生时都执行
    filenames = ["existing_file.txt", "non_existent_file.txt"]
    
    for filename in filenames:
        try:
            # 这里我们实际上不会创建文件，所以会引发FileNotFoundError
            # 调试提示: 在这里设置断点，观察异常如何被处理
            content = read_file(filename)
            print(f"文件内容: {content}")
        except FileNotFoundError as e:
            print(f"文件不存在: {e}")
        finally:
            # 调试提示: 在这里设置断点，观察finally块总是被执行
            print(f"尝试读取文件 {filename} 的操作已完成")

def example_raise():
    """手动引发异常示例"""
    print("\n===== 手动引发异常调试 =====")
    
    def validate_age(age):
        # 调试提示: 在这里设置断点，观察条件检查和异常引发
        if age < 0:
            raise ValueError("年龄不能为负数")
        if age > 150:
            raise ValueError("年龄不太可能超过150")
        return age
    
    ages = [-5, 25, 200]
    for age in ages:
        try:
            # 调试提示: 使用F11(单步进入)进入validate_age函数
            validated_age = validate_age(age)
            print(f"有效年龄: {validated_age}")
        except ValueError as e:
            print(f"年龄验证错误: {e}")

def example_custom_exception():
    """自定义异常示例"""
    print("\n===== 自定义异常调试 =====")
    
    class InsufficientFundsError(Exception):
        """余额不足异常"""
        def __init__(self, balance, amount):
            self.balance = balance
            self.amount = amount
            self.deficit = amount - balance
            super().__init__(f"余额不足。当前余额: {balance}，尝试支出: {amount}，差额: {self.deficit}")
    
    class BankAccount:
        def __init__(self, balance=0):
            self.balance = balance
        
        def withdraw(self, amount):
            # 调试提示: 在这里设置断点，观察条件检查和自定义异常的引发
            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)
            self.balance -= amount
            return amount
    
    # 创建账户并尝试取款
    account = BankAccount(100)
    withdrawals = [50, 60, 100]
    
    for amount in withdrawals:
        try:
            # 调试提示: 使用F11(单步进入)进入withdraw方法
            withdrawn = account.withdraw(amount)
            print(f"成功取款: {withdrawn}，剩余余额: {account.balance}")
        except InsufficientFundsError as e:
            # 调试提示: 在这里设置断点，观察自定义异常对象的属性
            print(f"取款失败: {e}")
            print(f"您需要额外存入 {e.deficit} 才能完成此次取款")

def main():
    print("===== 异常处理调试示例 =====")
    print("本示例演示如何在VSCode中调试异常情况")
    print("调试提示: 使用VSCode的异常断点功能，可以在任何异常发生时自动中断")
    print("设置方法: 在调试视图中点击'断点'部分的'+'按钮，选择'异常断点'")
    
    # 运行各个示例
    example_try_except()
    example_multiple_except()
    example_finally()
    example_raise()
    example_custom_exception()

if __name__ == "__main__":
    # 调试提示: 尝试设置异常断点，然后按F5开始调试
    main()
    print("\n程序执行完毕，尝试使用异常断点和普通断点结合来调试异常处理流程。")