"""
数据库初始化脚本
用于创建数据库表和初始数据
"""
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.database import init_db, drop_db


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="数据库管理工具")
    parser.add_argument(
        "action",
        choices=["init", "drop", "reset"],
        help="操作类型: init(初始化), drop(删除), reset(重置)",
    )

    args = parser.parse_args()

    if args.action == "init":
        print("🚀 正在初始化数据库...")
        init_db()

    elif args.action == "drop":
        confirm = input("⚠️  确定要删除所有表吗? (yes/no): ")
        if confirm.lower() == "yes":
            drop_db()
        else:
            print("❌ 操作已取消")

    elif args.action == "reset":
        confirm = input("⚠️  确定要重置数据库吗? 所有数据将丢失! (yes/no): ")
        if confirm.lower() == "yes":
            print("🗑️  正在删除旧表...")
            drop_db()
            print("🚀 正在创建新表...")
            init_db()
            print("✅ 数据库重置完成")
        else:
            print("❌ 操作已取消")


if __name__ == "__main__":
    main()
