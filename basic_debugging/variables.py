# 变量检查和监视示例
# 本示例演示如何在VSCode中检查和监视变量值

def main():
    # 基本变量类型
    simple_string = "Hello, VSCode Debugger!"
    simple_integer = 42
    simple_float = 3.14159
    simple_boolean = True
    
    # 复合数据类型
    my_list = [1, 2, 3, 4, 5]
    my_dict = {"name": "Python", "type": "语言", "level": "高级"}
    my_tuple = (10, 20, 30)
    my_set = {1, 2, 3, 3, 2, 1}  # 重复元素会被去除
    
    # 变量操作和修改
    # 调试提示: 在这里设置断点，然后观察变量如何变化
    print(f"初始列表: {my_list}")
    my_list.append(6)  # 添加元素
    print(f"添加后的列表: {my_list}")
    
    # 字典操作
    print(f"初始字典: {my_dict}")
    my_dict["version"] = "3.x"  # 添加新键值对
    print(f"修改后的字典: {my_dict}")
    
    # 变量作用域演示
    outer_var = "外部变量"
    
    def inner_function():
        inner_var = "内部变量"
        # 调试提示: 在这里设置断点，观察可以访问哪些变量
        print(f"内部函数可以访问外部变量: {outer_var}")
        print(f"内部函数定义的变量: {inner_var}")
        return inner_var
    
    result = inner_function()
    # 调试提示: 在这里设置断点，观察result的值，但inner_var不可访问
    print(f"函数返回值: {result}")
    
    # 调试技巧: 尝试在调试时修改变量值
    counter = 0
    for i in range(5):
        # 调试提示: 在循环内设置断点，然后在调试控制台修改i或counter的值
        counter += i
        print(f"循环 {i}: counter = {counter}")

if __name__ == "__main__":
    # 调试提示: 按F5开始调试，F9设置断点，F10单步执行，F11进入函数
    main()
    print("程序执行完毕，尝试使用不同的断点和调试命令来观察变量变化。")