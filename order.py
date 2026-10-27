# Food Delivery Order Processor
menu = {"Chicken Biriyani": 160, "Mutton Biriyani": 180, "Meals": 90, "Fish Meals": 120, "Poori Masala": 125, "Ginger Lemon Sugar cane juice": 150}

orders = [
    {"id": 101, "items": {"Chicken Biriyani": 2}},
    {"id": 102, "items": {"Mutton Biriyani": 1, "Meals": 1}},
    {"id": 103, "items": {"Fish Meals": 2}},
    {"id": 104, "items": {"Poori Masala": 2, "Meals": 5}},
    {"id": 105, "items": {"Chicken Biriyani": 1, "Ginger Lemon Sugar cane juice": 1}},
    {"id": 106, "items": {"Mutton Biriyani": 2}},
    {"id": 107, "items": {"Meals": 2, "Fish Meals": 1}},
    {"id": 108, "items": {"Chicken Biriyani": 2, "Poori Masala": 1}},
    {"id": 109, "items": {"Fish Meals": 1, "Ginger Lemon Sugar cane juice": 1}},
    {"id": 110, "items": {"Mutton Biriyani": 2, "Chicken Biriyani": 4, "Meals": 3, "Ginger Lemon Sugar cane juice": 3}}
]

def calculate_total(items):
    total = 0
    for item, quantity in items.items():
        total += menu[item] * quantity
    return total

def tdiscount(total):
    if total >= 800:
        return total * 0.10
    return 0

def delivery_charge(total):
    if total < 300:
        return 40
    return 0

def process_order(order):
    items = order["items"]
    if not items:
        print(f"Order {order['id']} is empty. Skipping.")
        return None
    for item, quantity in items.items():
        if item not in menu:
            print(f"Order {order['id']}: '{item}' is not on the menu.")
            return None
        if not isinstance(quantity, int) or quantity <= 0:
            print(f"Order {order['id']}: Invalid quantity for {item}.")
            return None
    subtotal = calculate_total(items)
    discount = tdiscount(subtotal)
    delivery = delivery_charge(subtotal)
    final_total = subtotal - discount + delivery

    print(f"\nOrder ID: {order['id']}")
    print("Items:", items)
    print(f"Subtotal: Rs. {round(subtotal, 2)}")
    print(f"Discount: Rs. {round(discount, 2)}")
    print(f"Delivery charge: Rs. {round(delivery, 2)}")
    print(f"Final bill: Rs. {round(final_total, 2)}")
    return {
        "id": order["id"],
        "subtotal": subtotal,
        "discount": discount,
        "delivery": delivery,
        "final_total": final_total
    }


processed_orders = []
for order in orders:
    result = process_order(order)

    if result is not None:
        processed_orders.append(result)
if processed_orders:
    highest_order = max(
        processed_orders,
        key=lambda order: order["final_total"]
    )
else:
    highest_order = None
def generate_report():
    total_revenue = sum(
        order["final_total"] for order in processed_orders
    )
    report = [
        "DAILY FOOD DELIVERY SALES REPORT",
        f"Total orders received: {len(orders)}",
        f"Successfully processed: {len(processed_orders)}",
        f"Invalid orders: {len(orders) - len(processed_orders)}",
        f"Total revenue: Rs. {round(total_revenue, 2)}"
    ]

    if highest_order is not None:
        report.extend([
            "",
            "HIGHEST-VALUE ORDER",
            f"Order ID: {highest_order['id']}",
            f"Final bill: Rs. {round(highest_order['final_total'], 2)}"
        ])

    report_text = "\n".join(report)
    print("\n" + report_text)
    with open("sales_report.txt", "w") as file:
        file.write(report_text)

generate_report()
print("\n--- Testing Invalid Orders ---")
process_order({"id": 111, "items": {}})
process_order({"id": 112, "items": {"Sushi": 2}})