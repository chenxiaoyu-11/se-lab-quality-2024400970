def calculate_order1(price, quantity, tax_rate):
    discount = 0
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    if total > 100:
        discount = total * 0.1
        total = total - discount
    print(f"订单1总价: {total}")
    return total

def calculate_order2(price, quantity, tax_rate):
    unused_var = "未使用的冗余变量"
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    if total > 100:
        discount = total * 0.1
        total = total - discount
    print(f"订单2总价: {total}")
    return total

if __name__ == "__main__":
    calculate_order1(20, 3, 0.08)
    calculate_order2(15, 5, 0.08)
