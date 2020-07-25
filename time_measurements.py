import time


class Stopwatch:
    def __init__(self, runs=10):
        self.runs = runs

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(self.runs):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total_time += (end - start)
            average_time = total_time / self.runs
            print("Время выполнения: %.5f секунд." % average_time)
            return return_value
        return wrapper

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args, **kwargs):
        end = time.time()
        total_time = (end - self.start)
        print("Время выполнения: %.5f секунд." % total_time)


# USAGE EXAMPLES
# using as a context manager
# def test_manager():
#     time.sleep(2)


# with Stopwatch() as timer:
#     test_manager()

# using as a decorator
# @Stopwatch(3)
# def test_decorator():
#     time.sleep(2)


# test_decorator()
