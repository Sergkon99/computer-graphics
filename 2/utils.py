import time
from functools import wraps

def log_method(func):
    # Декоратор логгирования
    @wraps(func)
    def wrap(self, *args, **kwargs):
        start = time.time()
        print(f'[Start] "{func.__name__}"')
        res = func(self, *args, **kwargs)
        print(f'[Working] "{func.__name__}" {round((time.time() - start)*1000, 2)} ms')
        print(f'[End] "{func.__name__}"')
        return res
    return wrap