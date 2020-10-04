# IMPORT STATEMENTS HERE
# FUNC TOOLS DECORATOR/WRAPPER
from functools import wraps
# TIME MODULE FOR SECONDS CALCULATION
import time


def benchmark_sec(function_wrapper):
    """
    Main functional wrapper code for function that will be used for further calling inbound functions
    :param function_wrapper: the function and args wrapped into one
    :return: wrap
    """

    # SET THE WRAPPER HERE
    @wraps(function_wrapper)
    def wrap(*args, **kwargs):
        """
        The inner wrapper function that will handle execution of the function
        :param args: The Positional arguments list.
        :param kwargs: The keyword arugments list.
        :return:
        """
        start_time = time.time()
        result = function_wrapper(*args, **kwargs)
        print("Function : %r | Args: (Positional : %r, Keyword : %r) | Elapsed Secs: %2.3f sec(s)" %
              (function_wrapper.__name__, args, kwargs, time.time() - start_time)
              )
        return result
    return wrap
