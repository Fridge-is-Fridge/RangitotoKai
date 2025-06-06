budget_price = 6
premium_price = budget_price * 1.5
delivery_cost = 5

budget_menu = {
    1 : "Kawakawa Spritzer",
    2 : "Pork and Puha Slider",
    3 : "Horopito Fish Collars",
    4 : "Kawakawa Muscles",
    5 : "Taro and Coconut Fritters",
    6 : "Kumara and Fennel Salad"
}

premium_menu = {
    7 : "Paua and Prawn Dumplings",
    8 : "Kina Canapes",
    9 : "Kumara and Truffle Ravioli",
    10 : "Manuka Smoked Salmon",
    11 : "Paua Porridge"
}

valid_pc = ["0620", "0630", "0632"]
all_orders = {}
order_num = 0


def print_menu():
    print("BUDGET MENU:")
    for k, v in budget_menu.items():
        print(f"{k}. {v} ${budget_price:.2f}")
    print("PREMIUM MENU:")
    for k, v in premium_menu.items():
        print(f"{k}. {v} ${premium_price:.2f}")



def get_order():
    ordered = []
    total_cost = 0
    name = input("What is the name for the order?")

    order_more = "yes"
    min_items = 3
    budget_list_end = 6
    prem_start = 7
    prem_end = 11


    while  order_more == "yes" or len(ordered) < min_items:
        try:
            item = int(input("Please enter the number of the item you would like (Theres a minimum of three items :P)"))
            if item in budget_menu:
                ordered.append(budget_menu[int(item)])
                total_cost += budget_price
            elif item in premium_menu:
                ordered.append(premium_menu[int(item)])
                total_cost += premium_price
            else:
                print("Invalid item number")
        except ValueError:
            print("Please enter a number")
        if len(ordered) >= 3 :
            order_more = input("Would you like to order another item??").lower()
        else:
            pass

    pick_deliver = input("Pick up or delivery?").lower()


    if pick_deliver == "delivery":
        postcode = input("What is your postal code?")
        if postcode in valid_pc:
            address = ""
            address = input("What is your address?")
            phone = int(input("What is your phone number?"))
            total_cost += delivery_cost
        else:
            print("unfortunately delivery is not available for your area, you will have to pick up your order")
            var = pick_deliver == "pick up"
    elif pick_deliver == "pick up":
        print("Your order will be ready for pickup")
    else:
        print("bro enter either 'pick up' or 'delivery'")
        pick_deliver = input("Pick-up or delivery?")

    return {
        "name": name,
        "method": pick_deliver,
        "items": ordered,
        "address": address,
        "phone": phone,
        "total_cost": total_cost
    }



def print_receipt(order, order_num):
    gst_excl = round(order["total_cost"] / 1.15, 2)
    print(f"\n--- Receipt for Order #{order_num} ---")
    print(f"Name: {order['name']}")
    print(f"Order type: {order['method']}")
    print(f"Items ordered: {order['items']}")
    print(f"Total (excluding GST): ${gst_excl}")
    print(f"Total (including GST): ${order['total_cost']:.2f}")

    if order["method"] == "delivery":
        print(f"Delivery address: {order['address']}")
        print(f"Phone: {order['phone']}")





print_menu()
order_yn = input("Would you like to place an order? (yes/no): ").lower()

while order_yn == "yes":
    order_num += 1
    order = get_order()
    print_receipt(order, order_num)
    all_orders[order_num] = order
    order_yn = input("\nWould you like to place another order? (yes/no): ").lower()

# Final summary
print("\n--- All Orders Summary ---")
for num, order in all_orders.items():
    print(f"\nOrder #{num}:")
    print(f"  Name: {order['name']}")
    print(f"  Items: {order['items']}")
    print(f"  Total: ${order['total_cost']:.2f}")





