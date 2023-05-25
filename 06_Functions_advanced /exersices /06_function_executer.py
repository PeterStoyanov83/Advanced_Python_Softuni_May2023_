def func_executor(*funcs):
    return '\n'.join([f"{func.__name__} - {func(*args)}" for func, args in funcs])
