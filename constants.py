"""
数学常量模块
提供常用的数学常量和转换因子
"""

import math

# 基础数学常量
PI = math.pi
E = math.e

# 黄金比例
GOLDEN_RATIO = (1 + math.sqrt(5)) / 2

# 常用角度（弧度）
DEG_TO_RAD = PI / 180
RAD_TO_DEG = 180 / PI


def get_constant_info():
    """获取所有常量信息"""
    return {
        "PI": PI,
        "E": E,
        "黄金比例": GOLDEN_RATIO,
        "角度转弧度": DEG_TO_RAD,
        "弧度转角度": RAD_TO_DEG
    }
