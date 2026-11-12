
# ONLINE SHOPPING APPLICATION

def calculate_total(price, quantity):

    if price < 0 or quantity < 0:
        raise ValueError("Invalid input")

    return price * quantity


def apply_discount(total, discount):

    if total < 0 or discount < 0 or discount > 100:
        raise ValueError("Invalid discount")

    return total - (total * discount / 100)


def calculate_final_amount(price, quantity, discount):

    total = calculate_total(price, quantity)

    final_amount = apply_discount(total, discount)

    return final_amount


if __name__ == "__main__":

    amount = calculate_final_amount(1000, 2, 10)

    print("Online Shopping Application")
    print("Final Shopping Amount:", amount)
