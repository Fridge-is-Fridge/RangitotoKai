budget_price = 6
premium_price = budget_price * 1.5

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




all_orders = {}
valid_pc = ["0620", "0630", "0632"]





def print_menu():

    for k, v in budget_menu.items():
        print("BUDGET MENU:")
        print(f"{k}. {v} ${float(budget_price)}")
    for k, v in premium_menu.items():
        print("PREMIUM MENU:")
        print(f"{k}. {v} ${float(premium_price)}")



def get_order():
    total_cost = 0
    name = input("What is the name for the order?")
    ordered = []
    min_items = 3
    budget_list_end = 6
    prem_start = 7
    prem_end = 11
    deliver_cost = 5
    order_more = "yes"
    while  order_more.lower() == "yes" or len(ordered) < min_items:
        order_stuff = int(input("What would you like to order? (Theres a minimum of three items :P)"))
        if 1 <= order_stuff <= budget_list_end:
            ordered.append(budget_menu[int(order_stuff)])
            total_cost = total_cost + budget_price
        elif prem_start <= order_stuff <= prem_end:
            ordered.append(premium_menu[int(order_stuff)])
            total_cost = total_cost + premium_price
        else:
            print("Enter a valid numerical input")
        if len(ordered) >= 3 :
            order_more = input("Would you like to order another item??")
        else:
            pass
    pick_deliver = input("Pick up or delivery?")
    if pick_deliver.lower() == "delivery":
        postcode = input("What is your postal code?")
        if postcode in valid_pc:
            print("ye")
            house_num = input("What is your house number?")
            street = input("What is your street name?")
            suburb = input("What is your suburb?")
            phone = int(input("What is your phone number?"))
            total_cost = total_cost + 5
        else:
            print("unfortunately delivery is not available for your area, you will have to pick up your order")
    elif pick_deliver.lower() == "pick up":
        print("alr your order will be ready for pickup")
    else:
        print("bro enter either 'pick up' or 'delivery'")
        pick_deliver = input("Pick-up or delivery?")

total_cost = 0
def print_receipt():
    gst_excl = total_cost / 1.15
    order1 = [name, pick_deliver, ordered, house_num, street, suburb, phone, gst_excl, total_cost ]
    n = len(order1)
    print(f"Name: {0}"
            f"Order type: {1}"
            f"Items ordered: {2}"
            f"Total excl GST: {float(7)}"
            f"Total incl GST: {float(8)}"
            )

    print(order1)
    order_yn = input("would you like to place another order?")
    all_orders[order_num] = order1


print(all_orders)


print_menu()
order_yn = input("Would you like to order?")
if order_yn == "yes":
    order_num = 0
    while order_yn == "yes":
        order_num = order_num + 1
        get_order()
        print_receipt()
        order_yn = input("Would you like to place another order")
else:
    print("Alright have a good day")





