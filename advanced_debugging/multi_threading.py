# 多线程调试示例
# 本示例演示如何在VSCode中调试多线程程序

import threading
import time
import random
from queue import Queue

# 共享资源
shared_counter = 0
counter_lock = threading.Lock()
print_lock = threading.Lock()

# 工作队列
work_queue = Queue()
result_queue = Queue()

def safe_print(message):
    """线程安全的打印函数"""
    with print_lock:
        print(message)

def increment_counter(thread_id, iterations):
    """增加共享计数器的函数"""
    global shared_counter
    
    for i in range(iterations):
        # 调试提示: 在这里设置断点，观察多个线程如何竞争锁
        time.sleep(random.random() * 0.1)  # 随机短暂延迟
        
        # 获取锁并修改共享资源
        with counter_lock:
            # 调试提示: 在这里设置断点，观察一次只有一个线程能执行这段代码
            current_value = shared_counter
            time.sleep(random.random() * 0.1)  # 模拟处理时间
            shared_counter = current_value + 1
            
        safe_print(f"线程 {thread_id}: 迭代 {i+1}/{iterations}, 计数器 = {shared_counter}")

def worker_thread(thread_id):
    """工作线程函数，从队列获取任务并处理"""
    safe_print(f"工作线程 {thread_id} 已启动")
    
    while True:
        # 从队列获取任务
        # 调试提示: 在这里设置断点，观察线程如何等待任务
        task = work_queue.get()
        
        # 检查是否是终止信号
        if task is None:
            safe_print(f"工作线程 {thread_id} 收到终止信号，退出")
            break
            
        # 处理任务
        # 调试提示: 在这里设置断点，观察不同线程如何处理不同任务
        task_id, task_data = task
        safe_print(f"线程 {thread_id} 正在处理任务 {task_id}: {task_data}")
        
        # 模拟处理时间
        time.sleep(random.random() * 0.5)
        
        # 将结果放入结果队列
        result = f"任务 {task_id} 的结果由线程 {thread_id} 处理完成"
        result_queue.put((task_id, result))
        
        # 标记任务完成
        work_queue.task_done()