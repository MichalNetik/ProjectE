def get_sum_of_single_multiplier(num: int, multiplier: int):
    """
    Get sum of an arithmetic sequence.
    Formula & explanation: https://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html
    """
    num_over_multiplier = num // multiplier
    return multiplier * num_over_multiplier * (num_over_multiplier + 1) // 2

def get_multiplies_sum(num: int):
    """
    Get a sum of a artihmetic sequence lesser than num for multipliers of 3 and 5.
    Subtract then sum of multipliers of 15.
    """
    num = num - 1
    result = 0

    result += get_sum_of_single_multiplier(num, 3)
    result += get_sum_of_single_multiplier(num, 5)
    result -= get_sum_of_single_multiplier(num, 15)
    return  result

