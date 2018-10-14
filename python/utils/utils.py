import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        total_time = time.time() - start_time

        print(
            'Test {test_name} run for: {total_time:3f} seconds.'.format(
                test_name=func.__name__,
                total_time=total_time
            )
        )

    return wrapper