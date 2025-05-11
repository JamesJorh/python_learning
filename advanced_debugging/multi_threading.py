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
            safe_print(f"工作线程 {thread_id} 收到终止信号，退出中...")
            work_queue.task_done()
            break
        
        # 处理任务
        task_id, task_data = task
        safe_print(f"工作线程 {thread_id} 处理任务 {task_id}: {task_data}")
        
        # 模拟处理时间
        time.sleep(random.random() * 0.5)
        
        # 计算结果并放入结果队列
        result = task_data * 2  # 简单的处理逻辑
        # 调试提示: 在这里设置断点，观察如何将结果放入另一个队列
        result_queue.put((task_id, result))
        
        # 标记任务完成
        work_queue.task_done()
    
    safe_print(f"工作线程 {thread_id} 已退出")

def result_processor():
    """结果处理线程函数"""
    safe_print("结果处理线程已启动")
    results = {}
    
    while True:
        try:
            # 从结果队列获取结果，设置超时以便能够检查终止标志
            # 调试提示: 在这里设置断点，观察如何从队列获取结果
            task_id, result = result_queue.get(timeout=1)
            safe_print(f"结果处理线程: 收到任务 {task_id} 的结果: {result}")
            results[task_id] = result
            result_queue.task_done()
        except Exception:
            # 检查是否所有工作线程都已完成且结果队列为空
            if work_queue.empty() and result_queue.empty() and all_workers_done:
                break
    
    safe_print("结果处理线程: 所有结果处理完毕")
    safe_print(f"最终结果: {results}")

def example_basic_threading():
    """基本线程示例"""
    print("\n===== 基本线程示例 =====")
    threads = []
    
    # 创建多个线程
    for i in range(3):
        # 调试提示: 在这里设置断点，观察线程的创建过程
        thread = threading.Thread(
            target=increment_counter, 
            args=(i+1, 5),
            name=f"Counter-Thread-{i+1}"
        )
        threads.append(thread)
        safe_print(f"创建线程 {i+1}")
    
    # 启动所有线程
    for i, thread in enumerate(threads):
        safe_print(f"启动线程 {i+1}")
        thread.start()
    
    # 等待所有线程完成
    for i, thread in enumerate(threads):
        # 调试提示: 在这里设置断点，观察主线程如何等待其他线程
        thread.join()
        safe_print(f"线程 {i+1} 已完成")
    
    safe_print(f"所有线程完成，最终计数器值: {shared_counter}")

def example_producer_consumer():
    """生产者-消费者模式示例"""
    print("\n===== 生产者-消费者模式示例 =====")
    global all_workers_done
    all_workers_done = False
    
    # 创建工作线程
    workers = []
    for i in range(3):
        # 调试提示: 在这里设置断点，观察工作线程的创建
        worker = threading.Thread(
            target=worker_thread, 
            args=(i+1,),
            name=f"Worker-{i+1}"
        )
        worker.daemon = True  # 设置为守护线程
        workers.append(worker)
        worker.start()
    
    # 创建结果处理线程
    result_thread = threading.Thread(
        target=result_processor,
        name="Result-Processor"
    )
    result_thread.daemon = True
    result_thread.start()
    
    # 添加任务到队列
    for i in range(10):
        # 调试提示: 在这里设置断点，观察如何向队列添加任务
        task_data = random.randint(1, 100)
        safe_print(f"主线程: 添加任务 {i+1} 到队列，数据: {task_data}")
        work_queue.put((i+1, task_data))
        time.sleep(random.random() * 0.3)  # 随机延迟
    
    # 添加终止信号
    for _ in range(len(workers)):
        work_queue.put(None)
    
    # 等待所有任务完成
    # 调试提示: 在这里设置断点，观察主线程如何等待队列清空
    work_queue.join()
    safe_print("主线程: 所有任务已完成")
    
    # 设置标志，通知结果处理线程可以退出
    all_workers_done = True
    
    # 等待结果处理线程完成
    result_thread.join()
    
    safe_print("主线程: 程序执行完毕")

def main():
    print("===== 多线程调试示例 =====")
    print("本示例演示如何在VSCode中调试多线程程序")
    print("调试提示: 在VSCode中，可以在调试控制台查看所有线程")
    print("在调试视图中，可以看到'调用堆栈'面板，其中显示了所有线程")
    print("您可以在不同线程之间切换，查看每个线程的状态")
    
    # 运行示例
    example_basic_threading()
    example_producer_consumer()

if __name__ == "__main__":
    # 调试提示: 按F5开始调试，然后观察多个线程的执行
    main()
    print("\n程序执行完毕，尝试在不同的线程中设置断点并观察执行流程。")
    print("多线程调试是一项高级技能，掌握它将帮助您解决复杂的并发问题。")