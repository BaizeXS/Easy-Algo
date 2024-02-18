import time
import math

# 设置测试的基数和指数
base = 2
repeat_times = 100000

for exp in [1, 10, 100, 1000]:
    # 测试 **
    start_time = time.time()
    for _ in range(repeat_times):
        base**exp
    end_time = time.time()
    time_with_operator = end_time - start_time

    # 测试内置 pow 函数
    start_time = time.time()
    for _ in range(repeat_times):
        pow(base, exp)
    end_time = time.time()
    time_with_builtin_pow = end_time - start_time

    # 测试 math.pow
    start_time = time.time()
    for _ in range(repeat_times):
        math.pow(base, exp)
    end_time = time.time()
    time_with_math_pow = end_time - start_time

    print(f"\nbase: {base}, exp: {exp}")
    print(f"Using ** operator: {time_with_operator} seconds")
    print(f"Using builtin pow: {time_with_builtin_pow} seconds")
    print(f"Using math.pow: {time_with_math_pow} seconds")
