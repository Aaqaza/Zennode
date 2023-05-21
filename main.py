# ZENNODE

products = {
    "A": 20,
    "B": 40,
    "C": 50
}

quantities = {}
gift_wraps = {}

for product in products:
    quantity = int(input(f"Enter the quantity of {product}:"))
    quantities[product] = quantity
    gift_wrap = input(f"Is {product} wrapped as a gift?(Yes/No)").lower() == "yes"
    gift_wraps[product] = gift_wrap

discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 5,
    "bulk_10_discount": 10,
    "tiered_50_discount": 50
}

subtotal = 0
discount_applied = None
discount_amount = 0

for product, quantity in quantities.items():
    subtotal += products[product] * quantity


if subtotal > 200:
    discount_applied = "flat_10_discount"
    discount_amount = discount_rules["flat_10_discount"]

elif any(quantity > 10 for quantity in quantities.values()):
    for product, quantity in quantities.items():
        if quantity > 10:
            discount_applied = "bulk_5_discount"
            discount_amount = (products[product] * quantity) * discount_rules["bulk_5_discount"] / 100
            break

elif sum(quantities.values()) > 20:
    discount_applied = "bulk_10_discount"
    discount_amount = subtotal * discount_rules["bulk_10_discount"] / 100

elif sum(quantities.values()) > 30 and any(quantity > 15 for quantity in quantities.values()):
    for product, quantity in quantities.items():
        if quantity > 15:
            discount_applied = "tiered_50_discount"
            discount_amount = (products[product] * (quantity - 15)) * discount_rules["tiered_50_discount"] / 100
            break

gift_wrap_fee = sum(quantity for product, quantity in quantities.items() if gift_wraps[product])
shipping = 5 * ((sum(quantities.values()) - 1) // 10 + 1)
total = subtotal - discount_amount + gift_wrap_fee + shipping

print("Product Details:")
for product, quantity in quantities.items():
    print(f"{product}: {quantity} * ${products[product]} = ${products[product] * quantity}")

print(f"\nSubtotal: ${subtotal}")

if discount_applied:
    print(f"Discount applied: {discount_applied}:${discount_amount:}")

print(f"Shipping Fee: ${shipping}")
print(f"Gift Wrap Fee: ${gift_wrap_fee}")
print(f"Total: ${total}")
