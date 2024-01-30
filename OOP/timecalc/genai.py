import time

class ExecutionTimer:
    def __init__(self, func):
        self.func = func

    def __call__(self,  *args, **kwargs):
        start_time = time.perf_counter()
        result = self.func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{self.func.__name__}() took {(end_time - start_time)*1000:.4f} ms")
        return result