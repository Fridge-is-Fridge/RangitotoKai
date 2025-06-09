#constants
BUDGET_PRICE = 6
PREMIUM_PRICE = BUDGET_PRICE * 1.5
DELIVERY_FEE = 5.00
VALID_POSTCODES = ["0620", "0630", "0632"]
MIN_ITEMS = 3
BUDGET_MENU = {
    1 : "Kawakawa Spritzer",
    2 : "Pork and Puha Slider",
    3 : "Horopito Fish Collars",
    4 : "Kawakawa Muscles",
    5 : "Taro and Coconut Fritters",
    6 : "Kumara and Fennel Salad"
}
PREMIUM_MENU = {
    7 : "Paua and Prawn Dumplings",
    8 : "Kina Canapes",
    9 : "Kumara and Truffle Ravioli",
    10 : "Manuka Smoked Salmon",
    11 : "Paua Porridge"
}


all_orders = {}
order_num = 0


def print_menu():
    print("BUDGET MENU:")
    for k, v in BUDGET_MENU.items():
        print(f"{k}. {v} ${BUDGET_PRICE:.2f}")
    print("PREMIUM MENU:")
    for k, v in PREMIUM_MENU.items():
        print(f"{k}. {v} ${PREMIUM_PRICE:.2f}")


def get_order():
    ordered = []
    total_cost = 0
    name = input("What is the name for the order?")
    order_more = "yes"
    while  order_more == "yes" or len(ordered) < MIN_ITEMS:
        try:
            item = int(input("Please enter the number of the item you would like (Theres a minimum of three items :P)"))
            if item in BUDGET_MENU:
                ordered.append(BUDGET_MENU[int(item)])
                total_cost += BUDGET_PRICE
            elif item in PREMIUM_MENU:
                ordered.append(PREMIUM_MENU[int(item)])
                total_cost += PREMIUM_PRICE
            else:
                print("Invalid item number")
        except ValueError:
            print("Please enter a number")
        if len(ordered) >= MIN_ITEMS :
            order_more = input("Would you like to order another item??").lower()
        else:
            pass

    pick_deliver = input("Pick up or delivery?").lower()

    address = "Unknown"
    phone = "Unknown"
    if pick_deliver == "delivery":
        postcode = input("What is your postal code?")
        if postcode in VALID_POSTCODES:
            address = input("What is your address?")
            phone = int(input("What is your phone number?"))
            total_cost += DELIVERY_FEE
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
    print(f"\nOrder {order_num}:")
    print(f"Name: {order['name']}")
    print(f"Order type: "
          f"{order[*'method']}")
    print(f"Items ordered: {order['items']}")
    print(f"Total (excluding GST): ${gst_excl}")
    print(f"Total (including GST): ${order['total_cost']:.2f}")

    if order["method"] == "delivery":
        print(f"Delivery address: {order['address']}")
        print(f"Phone: {order['phone']}")
        print(f"Delivery fee ${DELIVERY_FEE:.2F}")





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
    print(f"\nOrder {num}:")
    print(f"  Name: {order['name']}")
    print(f"  Items: {order['items']}")
    print(f"  Total: ${order['total_cost']:.2f}")





