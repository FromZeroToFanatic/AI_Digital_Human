#!/usr/bin/env python
"""Django的命令行工具，用于执行管理任务。"""
import os
import sys


def main():
    """执行管理任务。"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入Django。请确认它已安装并且在您的PYTHONPATH环境变量中可用。您是否忘记激活虚拟环境？"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
