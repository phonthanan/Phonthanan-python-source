# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal
subtotal = item_price * quantity

# TODO: Calculate discount amount
discount_amount = subtotal * (discount_percent / 100)

# TODO: Calculate price after discount
price_after_discount = subtotal - discount_amount

# TODO: Calculate tax amount
tax_amount = price_after_discount * (tax_percent / 100)

# TODO: Calculate final total
final_total = price_after_discount + tax_amount

# TODO: Display itemized receipt
print(f"subtotal{subtotal} baht, discount{discount_amount} baht, price after discount{price_after_discount} baht, tax{tax_amount} baht, {final_total} baht")