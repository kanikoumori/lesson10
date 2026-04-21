from decimal import Decimal

def postTaxPrice(price):
    price = Decimal(str(price))
    return price * Decimal("1.1")