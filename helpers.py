import time

def execute(func, *args, show_result=True):
    t1 = time.perf_counter()
    result = func(*args)
    t2 = time.perf_counter()
    diff = t2 - t1
    if show_result:
        print(f"{func.__name__}: {result} in {diff:.10f}s")
    else:
        print(f"{func.__name__} completed in {diff:.10f}s")
    return result, diff