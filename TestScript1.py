from Utils.StandardBenchMarker import benchmark_sec
import time


@benchmark_sec
def waiter_testing(total_wait):
    time.sleep(total_wait)


if __name__ == '__main__':
    waiter_testing(total_wait=2)
    waiter_testing(3)
    my_temp_list = [4]
    waiter_testing(*my_temp_list)