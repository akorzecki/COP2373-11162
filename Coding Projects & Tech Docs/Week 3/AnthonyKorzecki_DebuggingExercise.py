def calculate_discount(price, discount_rate):

    # Calculate the discount amount based on the price and discount rate.
    discount_amount = price * discount_rate
    return discount_amount


def apply_discount(price, discount_amount):

    # Apply the discount amount to the original price and return the new price.
    new_price = price - discount_amount
    return new_price


def main():

    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        # The original error occured here. "500" is a string, because of the
        # quotation marks. Removing those marks makes it an integer
        # (which works flawlessly).
        {"name": "Tablet", "price": 500, "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05},
    ]

    for product in products:
        # this try block (if statement below) checks if the price and
        # discount_rate are both ints or floats, in order to prevent
        # a string or some other form of data being passed into
        # the math equation (which would break the math, of course)
        try:
            price = product["price"]
            discount_rate = product["discount_rate"]

            # if its not an instance of an int or float, raise the TypeError
            # written below. This error has to be called later
            # in the Except block with the {err} variable.
            if not isinstance(price, (int, float)) or not isinstance(
                discount_rate, (int, float)
            ):
                # Explaining the error to the user and providing a solution.
                raise TypeError(
                    f"Expected numeric values for price and discount rate, "
                    f"but received price type '{type(price).__name__}' and "
                    f"discount_rate type '{type(discount_rate).__name__}'. "
                    "Please change price and/or"
                    "discount_rate to an Int or Float"
                )

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {product['name']}")
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
            print()

        # This is where that TypeError I created gets called. Using that
        # {err} variable allows me to move my message from the raised Typerror
        # generated in the try block. This architecture allows more error
        # messages to be implemented (say, if a product name didn't exist).
        except TypeError as err:
            print(f"Error processing '{product['name']}': {err}.")


if __name__ == "__main__":
    main()
