def add_vat(price, rate=0.2):
    return round(price * (1 + rate), 2)


def apply_discount(price, percent):
    return round(price * (1 - percent / 100), 2)
