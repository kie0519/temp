#!/usr/bin/env python3
"""
简单的 Python 示例程序
用于 Git 练习
"""

def greet(name):
    """向指定的人打招呼"""
    return f"你好，{name}！欢迎使用 Git 练习项目！"

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

def interactive_calculator():
    """交互式计算器"""
    print("\n=== 交互式计算器 ===")
    print("支持操作: +（加）, -（减）, *（乘）, /（除）")
    print("输入 'q' 退出\n")

    while True:
        try:
            num1 = input("请输入第一个数字: ")
            if num1.lower() == 'q':
                print("感谢使用计算器！")
                break

            operator = input("请输入运算符 (+, -, *, /): ")
            if operator.lower() == 'q':
                print("感谢使用计算器！")
                break

            num2 = input("请输入第二个数字: ")
            if num2.lower() == 'q':
                print("感谢使用计算器！")
                break

            num1 = float(num1)
            num2 = float(num2)

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("无效的运算符！")
                continue

            print(f"结果: {num1} {operator} {num2} = {result}\n")

        except ValueError:
            print("错误：请输入有效的数字！\n")

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

    # 启动交互式计算器
    use_interactive = input("\n是否使用交互式计算器？(y/n): ")
    if use_interactive.lower() == 'y':
        interactive_calculator()

if __name__ == "__main__":
    main()
