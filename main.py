budget_menu = {1 : "Kawakawa Spritzer",2 : "Pork and Puha Slider",3 : "Horopito Fish Collars",4 : "Kawakawa Muscles",5 : "Taro and Coconut Fritters",6 : "Kumara and Fennel Salad"}
premium_menu = {7 : "Paua and Prawn Dumplings",8 : "Kina Canapes", 9 : "Kumara and Truffle Ravioli",10 : "Manuka Smoked Salmon", 11 : "Paua Porridge" }
budget_price = 6
premium_price = budget_price * 1.5
all_orders = {}
valid_pc = ["0620", "0630", "0632"]
total_cost = 0
house_num = 0
street = ""
suburb = ""
phone = ""
ordered = []
order_num = 0
order_more = "yes"


name = input("What is the name for the order?")
print(budget_menu)
print(premium_menu)


#I know there's magic numbers ill deal with them laters
order_yn = input("Would you like to order?")
while order_yn.lower() == "yes":
    order_num =+ 1
    if order_more.lower() == "yes" :
        while  order_more.lower() == "yes" or len(ordered) < 3:
            order_stuff = int(input("What would you like to order? (Theres a minimum of three items :P)"))
            if 1 <= order_stuff <= 6:
                ordered.append(budget_menu[int(order_stuff)])
                total_cost = total_cost + budget_price
                print(ordered)
            elif 7 <= order_stuff <= 11:
                ordered.append(premium_menu[int(order_stuff)])
                total_cost = total_cost + premium_price
                print(ordered)
            else:
                print("Enter a valid numerical input")
            if len(ordered) >= 3 :
                order_more = input("Would you like to order another item??")
            else:
                pass
        pick_deliver = input("Pick up or delivery?")
        if pick_deliver.lower() == "delivery":
            postcode = input("What is your postal code?")
            if postcode == "0620" or postcode == "0630" or postcode == "0632":
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
    else:
        print("Mkay, have a good dayy")



    order1 = [name, ordered, pick_deliver, house_num, street, suburb, phone, total_cost]
    print(order1)

    new_order = input("would you like to place another order?")


    all_orders[order_num] = order1


    print(all_orders)








"""

    pick_deliver = input("Pick-up or delivery?")

    while pick_deliver.lower() != "pick-up" or "pick up" or "delivery":
        if pick_deliver.lower() == "pick up" or "pick-up":
            print("alr")
            break
        elif pick_deliver.lower() == "delivery":
            try:
                postcode = input("What is your postal code?")
            except ValueError :
                while postcode != int:
                    print("enter a number bro")
                    postcode = input("What is your postal code?")
                    if postcode == int:
                        break
            break
        else:
            print("bro enter either 'pick up' or 'delivery'")
            pick_deliver = input("Pick-up or delivery?")
"""

