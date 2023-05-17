def discount_price(price, discount):
    def apply_discount():
        nonlocal price,discount
        price = price - (price * discount)
    apply_discount()
    return price

discount_price(100, 0.1)