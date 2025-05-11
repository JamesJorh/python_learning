# VSCode Python 调试学习项目

这个项目包含了一系列专为学习VSCode中Python调试功能而设计的示例代码。

## 项目结构

- `basic_debugging/`: 基础调试示例
  - `variables.py`: 变量检查和监视
  - `control_flow.py`: 控制流程调试
  - `functions.py`: 函数调用和堆栈跟踪

- `advanced_debugging/`: 高级调试示例
  - `conditional_breakpoints.py`: 条件断点示例
  - `exception_handling.py`: 异常处理调试
  - `multi_threading.py`: 多线程调试

- `real_world_examples/`: 实际应用场景
  - `data_processing.py`: 数据处理调试
  - `api_client.py`: API客户端调试

## 如何使用

1. 在VSCode中打开此项目
2. 安装Python扩展（如果尚未安装）
3. 打开任意示例文件
4. 设置断点（点击行号左侧）
5. 按F5或点击调试按钮开始调试

## VSCode调试快捷键

- F5: 开始/继续调试
- F10: 单步跳过（Step Over）
- F11: 单步进入（Step Into）
- Shift+F11: 单步跳出（Step Out）
- F9: 切换断点
- Ctrl+Shift+F5: 重启调试
- Shift+F5: 停止调试

## 调试配置

项目包含了`.vscode/launch.json`文件，已预先配置好调试设置。