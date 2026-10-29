# -*- coding: utf-8 -*-
"""第一个 Python 项目 —— 按 F5 运行"""

import sys


def main():
    print("=" * 40)
    print("Hello, Python!")
    print("解释器版本:", sys.version.split()[0])
    print("=" * 40)

    a = [3, 1, 4, 1, 5]
    print("列表      :", a)
    print("求和      :", sum(a))
    print("最大/最小 :", max(a), "/", min(a))
    print("排序后    :", sorted(a))

    for i, x in enumerate(a):
        print(f"  a[{i}] = {x}")

    print("=" * 40)


if __name__ == "__main__":
    main()
