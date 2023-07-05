from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    sum_arr = 0
    for i in number_list:
        sum_arr += Decimal(i)
    getcontext().prec = signs_count
    res = sum_arr / Decimal(len(number_list))
    return res