import time


def measure_execution_time(func):
    def wrapper():
        start_time = time.time()
        func()
        print("--- %s seconds ---" % (time.time() - start_time))

    return wrapper
