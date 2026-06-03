import traceback
from functools import wraps
from typing import Callable

from utils.logger import logger


def logger_wrapper(func: Callable) -> Callable:
    """
    Decorator to log exceptions and return None

    Args:
        func (Callable): input function

    Returns:
        Callable: function with logger
    """

    @logger.catch
    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            tb = "".join(traceback.TracebackException.from_exception(e))
            logger.error(f"[{func.__name__}] Error:\n{tb}")
            return None

    return wrap
