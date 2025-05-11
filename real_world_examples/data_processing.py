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
        print(f"读取CSV文件错误: {e}")
    return sales_data