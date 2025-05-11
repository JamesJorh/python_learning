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