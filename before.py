def calculate_total(subtotal: float, tax_rate: float) -> float:
    tax = subtotal * tax_rate
    total = subtotal + tax
    if total > 100:
        discount = total * 0.1
        total -= discount
    return total

def calculate_order(order_name: str, price: float, quantity: int, tax_rate: float) -> float:
    subtotal = price * quantity
    total = calculate_total(subtotal, tax_rate)
    print(f"{order_name}总价: {total}")
    return total

if __name__ == "__main__":
    calculate_order("订单1", 20, 3, 0.08)
    calculate_order("订单2", 15, 5, 0.08)
