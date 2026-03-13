

def calculate_discount(price, discount_percent):
    try:
        price = float(price)
        discount_percent = float(discount_percent)

        if discount_percent >= 20:
            new_price = price * (1 - (discount_percent / 100))
            return new_price
        else:
            raise ValueError("Discount percent must be greater than 20")
    except ValueError as e:
        print(f"Error: {e}")
        return None

price = input("Enter the price of the item: ")
discount_percent = input("Enter the discount percent: ")
new_price = calculate_discount(price, discount_percent)

print(f"The new price after discount is: {new_price}")