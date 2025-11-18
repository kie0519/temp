# CLI 计算器

## 概述
命令行版本的智能计算器，提供基础的数学运算功能。

## 功能特性
- ✅ 基础四则运算（加减乘除）
- ✅ 科学计算（幂、模、平方根、绝对值）
- ✅ 交互式计算器模式
- ✅ 数学常量支持（PI、E、黄金比例）

## 安装依赖

```bash
cd backend/cli
pip install -r requirements.txt
```

## 使用方法

### 直接运行
```bash
python calculator_cli.py
```

### 使用示例
```python
from calculator_cli import add, multiply, power

result = add(10, 5)      # 15
result = multiply(3, 4)  # 12
result = power(2, 3)     # 8
```

## 文件说明
- `calculator_cli.py`: 主程序，包含所有计算函数
- `constants.py`: 数学常量定义
- `requirements.txt`: Python 依赖包

## 开发计划
- [ ] 添加单位测试
- [ ] 支持表达式解析（如 "2+3*4"）
- [ ] 添加历史记录功能
- [ ] 支持自定义函数

---
**维护者**: zuojunwei  
**最后更新**: 2025-11-17
