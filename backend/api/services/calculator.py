"""
计算服务
提供基础计算和科学计算功能
"""
import re
import math
from typing import Union


class CalculatorService:
    """计算器服务类"""

    # 支持的数学常量
    CONSTANTS = {
        "pi": math.pi,
        "e": math.e,
        "tau": math.tau,
    }

    # 支持的数学函数
    FUNCTIONS = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "log": math.log,
        "log10": math.log10,
        "exp": math.exp,
        "abs": abs,
        "pow": pow,
    }

    @classmethod
    def evaluate(cls, expression: str) -> Union[float, int]:
        """
        计算数学表达式

        Args:
            expression: 数学表达式字符串

        Returns:
            Union[float, int]: 计算结果

        Raises:
            ValueError: 表达式无效或包含不安全的内容
            ZeroDivisionError: 除零错误
        """
        # 清理表达式
        expression = expression.strip()

        # 安全检查 - 防止代码注入
        if not cls._is_safe_expression(expression):
            raise ValueError("表达式包含不安全的内容")

        try:
            # 替换常量
            for name, value in cls.CONSTANTS.items():
                expression = re.sub(rf"\b{name}\b", str(value), expression, flags=re.IGNORECASE)

            # 创建安全的命名空间
            safe_dict = {
                "__builtins__": {},
                **cls.FUNCTIONS,
            }

            # 计算结果
            result = eval(expression, safe_dict)

            # 验证结果类型
            if not isinstance(result, (int, float)):
                raise ValueError("表达式必须返回数值结果")

            return result

        except ZeroDivisionError:
            raise ZeroDivisionError("除数不能为零")
        except SyntaxError as e:
            raise ValueError(f"表达式语法错误: {str(e)}")
        except Exception as e:
            raise ValueError(f"计算错误: {str(e)}")

    @staticmethod
    def _is_safe_expression(expression: str) -> bool:
        """
        检查表达式是否安全

        Args:
            expression: 表达式字符串

        Returns:
            bool: 是否安全
        """
        # 禁止的关键字和字符
        dangerous_patterns = [
            r"__",  # 双下划线 (防止访问私有属性)
            r"import",  # 导入语句
            r"exec",  # 执行代码
            r"eval",  # 嵌套eval
            r"compile",  # 编译代码
            r"open",  # 文件操作
            r"input",  # 输入
            r"__builtins__",  # 内置函数
            r"globals",  # 全局变量
            r"locals",  # 本地变量
            r"vars",  # 变量
            r"dir",  # 目录
        ]

        for pattern in dangerous_patterns:
            if re.search(pattern, expression, re.IGNORECASE):
                return False

        return True

    @classmethod
    def validate_expression(cls, expression: str) -> tuple[bool, str]:
        """
        验证表达式是否有效

        Args:
            expression: 表达式字符串

        Returns:
            tuple[bool, str]: (是否有效, 错误信息)
        """
        if not expression or not expression.strip():
            return False, "表达式不能为空"

        if len(expression) > 1000:
            return False, "表达式过长 (最多1000字符)"

        if not cls._is_safe_expression(expression):
            return False, "表达式包含不安全的内容"

        try:
            cls.evaluate(expression)
            return True, ""
        except Exception as e:
            return False, str(e)
