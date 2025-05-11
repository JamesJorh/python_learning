# 条件断点示例
# 本示例演示如何在VSCode中使用条件断点进行高级调试


def main():
    print("===== 条件断点示例 =====")
    print("条件断点允许您在特定条件满足时才触发断点")
    print("在VSCode中设置条件断点的方法:")
    print("1. 先设置普通断点(点击行号左侧)")
    print("2. 右键点击断点，选择'编辑断点'")
    print("3. 输入条件表达式(例如: i > 5)")
    print("\n下面是几个练习条件断点的例子:\n")

    # 示例1: 循环中的条件断点
    print("示例1: 循环中的条件断点")
    print("调试提示: 在for循环行设置条件断点 'i > 5'，只有当i大于5时才会触发")
    for i in range(10):
        # 在这行设置条件断点: i > 5
        result = i * i
        print(f"i = {i}, i² = {result}")

    # 示例2: 列表处理中的条件断点
    print("\n示例2: 列表处理中的条件断点")
    print(
        "调试提示: 在处理列表元素的行设置条件断点 'num % 3 == 0'，只在处理能被3整除的数时触发"
    )
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in numbers:
        # 在这行设置条件断点: num % 3 == 0
        square = num**2
        print(f"数字: {num}, 平方: {square}")

    # 示例3: 字典处理中的条件断点
    print("\n示例3: 字典处理中的条件断点")
    print("调试提示: 在处理字典项的行设置条件断点 'value > 100'，只在值大于100时触发")
    items = {"item1": 50, "item2": 120, "item3": 75, "item4": 200, "item5": 30}
    for key, value in items.items():
        # 在这行设置条件断点: value > 100
        tax = value * 0.1
        print(f"{key}: 价格 = {value}, 税 = {tax}")

    # 示例4: 复杂条件断点
    print("\n示例4: 复杂条件断点")
    print(
        '调试提示: 尝试设置更复杂的条件断点，如 \'person["age"] > 30 and person["salary"] > 50000\''
    )
    people = [
        {"name": "张三", "age": 25, "salary": 40000},
        {"name": "李四", "age": 35, "salary": 60000},
        {"name": "王五", "age": 45, "salary": 30000},
        {"name": "赵六", "age": 28, "salary": 55000},
        {"name": "钱七", "age": 38, "salary": 70000},
    ]
    for person in people:
        # 在这行设置条件断点:
        bonus = person["salary"] * 0.15
        print(
            f"{person['name']}: 年龄 = {person['age']}, 薪资 = {person['salary']}, 奖金 = {bonus}"
        )

    # 示例5: 使用函数作为条件
    print("\n示例5: 使用函数作为条件")
    print("调试提示: 在VSCode中，条件表达式可以调用函数，例如 'is_prime(i)'")

    def is_prime(n):
        """检查一个数是否为质数"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    for i in range(1, 20):
        # 在这行设置条件断点: is_prime(i)
        print(f"{i} 是质数: {is_prime(i)}")


if __name__ == "__main__":
    # 调试提示: 按照上述说明设置条件断点，然后按F5开始调试
    main()
    print("\n程序执行完毕，尝试使用不同的条件断点来控制调试过程。")
    print("条件断点是提高调试效率的重要工具，特别是在处理大型循环或复杂数据结构时。")
