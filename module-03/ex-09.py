def cost_delivery(*quantity, discount = 0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має \
        значення 0."""
    for i in quantity:
        if i > 1:
            cost = 5 + (i - 1) * 2
            if discount != 0:
                cost = cost - (cost * discount)
        else:
            if discount != 0:
                cost = 5 - (5 * discount)
            else:
                cost = 5
        return(cost)

