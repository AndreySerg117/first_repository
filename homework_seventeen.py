def whole_number(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return result + 10
        return result
    return wrapper


@whole_number
def print_number(number):
    return number


print(print_number(10))
print(print_number(5.5))
