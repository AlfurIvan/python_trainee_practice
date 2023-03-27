"""Task 3: make a decorator, that catches the exception, logs and reraise it"""

import logging


def exception_logger(func):
    def _wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as error:
            logging.exception(f"in __{func.__name__}()__ an error __{str(error).upper()}__, bad.")
            raise
    return _wrapper


@exception_logger
def div_by_zero():
    a = 1
    b = a/0


div_by_zero()
