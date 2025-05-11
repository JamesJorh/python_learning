# 数据处理调试示例
# 本示例演示如何在VSCode中调试数据处理流程

import csv
import json
import os
from datetime import datetime

# 模拟数据文件路径
CSV_FILE = "sales_data.csv"
JSON_FILE = "product_data.json"
OUTPUT_FILE = "sales_report.txt"

# 创建示例CSV数据文件
def create_sample_csv():
    """创建示例销售数据CSV文件"""
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["日期", "产品ID", "数量", "单价"])
        writer.writerow(["2023-01-15", "P001", "5", "100.00"])
        writer.writerow(["2023-01-16", "P002", "3", "150.00"])
        writer.writerow(["2023-01-16", "P001", "2", "100.00"])
        writer.writerow(["2023-01-17", "P003", "1", "200.00"])
        writer.writerow(["2023-01-18", "P002", "4", "150.00"])
        writer.writerow(["2023-01-19", "P004", "2", "120.00"])
        writer.writerow(["2023-01-20", "P001", "3", "100.00"])
        # 添加一个错误数据行用于调试
        writer.writerow(["2023-01-21", "P005", "错误", "90.00"])

# 创建示例JSON数据文件
def create_sample_json():
    """创建示例产品数据JSON文件"""
    products = {
        "P001": {"名称": "笔记本电脑", "类别": "电子产品", "供应商": "A公司"},
        "P002": {"名称": "智能手机", "类别": "电子产品", "供应商": "B公司"},
        "P003": {"名称": "办公桌", "类别": "家具", "供应商": "C公司"},
        "P004": {"名称": "办公椅", "类别": "家具", "供应商": "C公司"}
        # 注意：故意不包含P005，用于演示错误处理
    }
    with open(JSON_FILE, 'w', encoding='utf-8') as file:
        json.dump(products, file, ensure_ascii=False, indent=4)

# 读取CSV销售数据
def read_sales_data():
    """读取销售数据CSV文件"""
    sales_data = []
    try:
        # 调试提示: 在这里设置断点，观察文件读取过程
        with open(CSV_FILE, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # 调试提示: 在这里设置断点，观察每行数据的处理
                sales_data.append(row)
    except Exception as e:
        print(f"读取销售数据时出错: {e}")
    return sales_data

# 读取JSON产品数据
def read_product_data():
    """读取产品数据JSON文件"""
    try:
        # 调试提示: 在这里设置断点，观察JSON文件的读取
        with open(JSON_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"读取产品数据时出错: {e}")
        return {}

# 处理销售数据
def process_sales_data(sales_data, product_data):
    """处理销售数据，计算总销售额和按产品分类的销售统计"""
    # 初始化结果字典
    results = {
        "总销售额": 0.0,
        "按日期统计": {},
        "按产品统计": {},
        "按类别统计": {},
        "错误记录": []
    }
    
    # 处理每条销售记录
    for record in sales_data:
        try:
            # 调试提示: 在这里设置断点，观察每条记录的处理过程
            date = record["日期"]
            product_id = record["产品ID"]
            quantity = int(record["数量"])  # 可能引发ValueError
            price = float(record["单价"])  # 可能引发ValueError
            
            # 计算该条记录的销售额
            sale_amount = quantity * price
            
            # 更新总销售额
            results["总销售额"] += sale_amount
            
            # 按日期统计
            if date not in results["按日期统计"]:
                results["按日期统计"][date] = 0.0
            results["按日期统计"][date] += sale_amount
            
            # 按产品统计
            if product_id not in results["按产品统计"]:
                results["按产品统计"][product_id] = {
                    "销售额": 0.0,
                    "销售量": 0
                }
            results["按产品统计"][product_id]["销售额"] += sale_amount
            results["按产品统计"][product_id]["销售量"] += quantity
            
            # 按类别统计 (需要从产品数据中获取类别信息)
            if product_id in product_data:
                category = product_data[product_id]["类别"]
                if category not in results["按类别统计"]:
                    results["按类别统计"][category] = 0.0
                results["按类别统计"][category] += sale_amount
            else:
                # 调试提示: 在这里设置断点，观察未找到产品信息的情况
                results["错误记录"].append({
                    "记录": record,
                    "错误": f"未找到产品信息: {product_id}"
                })
                
        except ValueError as e:
            # 调试提示: 在这里设置断点，观察数据转换错误的情况
            results["错误记录"].append({
                "记录": record,
                "错误": f"数据格式错误: {e}"
            })
        except Exception as e:
            # 调试提示: 在这里设置断点，观察其他错误
            results["错误记录"].append({
                "记录": record,
                "错误": f"处理错误: {e}"
            })
    
    return results

# 生成销售报告
def generate_sales_report(results):
    """生成销售报告"""
    # 调试提示: 在这里设置断点，观察报告生成过程
    report = []
    report.append("===== 销售数据分析报告 =====")
    report.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    
    # 总销售额
    report.append(f"总销售额: ¥{results['总销售额']:.2f}")
    report.append("")
    
    # 按日期统计
    report.append("===== 按日期统计 =====")
    for date, amount in sorted(results["按日期统计"].items()):
        report.append(f"{date}: ¥{amount:.2f}")
    report.append("")
    
    # 按产品统计
    report.append("===== 按产品统计 =====")
    for product_id, data in results["按产品统计"].items():
        report.append(f"产品ID: {product_id}")
        report.append(f"  销售量: {data['销售量']}")
        report.append(f"  销售额: ¥{data['销售额']:.2f}")
    report.append("")
    
    # 按类别统计
    report.append("===== 按类别统计 =====")
    for category, amount in results["按类别统计"].items():
        report.append(f"{category}: ¥{amount:.2f}")
    report.append("")
    
    # 错误记录
    if results["错误记录"]:
        report.append("===== 错误记录 =====")
        for i, error in enumerate(results["错误记录"], 1):
            report.append(f"错误 #{i}:")
            report.append(f"  记录: {error['记录']}")
            report.append(f"  错误: {error['错误']}")
    
    return "\n".join(report)

# 保存报告到文件
def save_report(report, filename):
    """保存报告到文件"""
    try:
        # 调试提示: 在这里设置断点，观察文件写入过程
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(report)
        return True
    except Exception as e:
        print(f"保存报告时出错: {e}")
        return False

def main():
    print("===== 数据处理调试示例 =====")
    print("本示例演示如何调试数据处理流程")
    
    # 创建示例数据文件
    print("\n创建示例数据文件...")
    create_sample_csv()
    create_sample_json()
    
    # 读取数据
    print("\n读取销售和产品数据...")
    sales_data = read_sales_data()
    product_data = read_product_data()
    
    print(f"读取了 {len(sales_data)} 条销售记录")
    print(f"读取了 {len(product_data)} 个产品信息")
    
    # 处理数据
    print("\n处理销售数据...")
    # 调试提示: 在这里设置断点，然后使用F11(单步进入)进入处理函数
    results = process_sales_data(sales_data, product_data)
    
    # 生成报告
    print("\n生成销售报告...")
    report = generate_sales_report(results)
    
    # 保存报告
    print("\n保存报告到文件...")
    if save_report(report, OUTPUT_FILE):
        print(f"报告已保存到 {OUTPUT_FILE}")
    
    # 显示报告
    print("\n===== 报告内容 =====")
    print(report)
    
    # 清理示例文件
    print("\n清理示例文件...")
    for file in [CSV_FILE, JSON_FILE, OUTPUT_FILE]:
        if os.path.exists(file):
            os.remove(file)

if __name__ == "__main__":
    # 调试提示: 按F5开始调试，使用断点观察数据处理流程
    main()
    print("\n程序执行完毕，尝试在不同的数据处理阶段设置断点并观察执行流程。")
    print("数据处理调试是实际工作中最常见的场景之一，掌握它将大大提高您的工作效率。")