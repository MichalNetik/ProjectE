def _fibonacci_generator(num: int):
    """
    Yield fibonacci numbers which are lesser than num.
    """
    previous_number = 0
    current_number = 1

    yield previous_number
    yield current_number

    while (previous_number + current_number) < num:
      previous_number, current_number = current_number, previous_number + current_number
      yield current_number

def get_fibonacci_sum(num: int):
    """
    Iterate over all fibonacci numbers returned by _fibonacci_generator and sum the even ones.
    """
    result = 0
    for fib_num in _fibonacci_generator(num):
        if fib_num % 2 == 0:
            result += fib_num

    return result
