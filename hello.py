#!/usr/bin/env python3
"""
简单的 Python 示例程序
用于 Git 练习
"""

def greet(name):
    """向指定的人打招呼"""
    return f"Hello, {name}!"

def add(a, b):
    """加法运算"""
    return a + b

def subtract(a, b):
    """减法运算"""
    return a - b

def multiply(a, b):
    """乘法运算"""
    return a * b

def divide(a, b):
    """除法运算"""
    if b == 0:
        return "错误：除数不能为零"
    return a / b

def main():
    """主函数"""
    print(greet("Git 学习者"))
    print("欢迎来到 Git 练习项目！")
    print("这是你的第一个提交文件。")
    print("\n--- 计算器功能演示 ---")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")

if __name__ == "__main__":
    main()
