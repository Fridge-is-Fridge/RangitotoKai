budget_price = 6
premium_price = budget_price * 1.5


budget_menu = [
    {
        "id": 1,
        "name": "Kawakawa Spritzer",
        "price": budget_price
    },
    {
        "id": 2,
        "name": "Pork and Puha Slider",
        "price": budget_price
    },
    {3 : "Horopito Fish Collars"},{4 : "Kawakawa Muscles"},{5 : "Taro and Coconut Fritters"},{6 : "Kumara and Fennel Salad"}]

































premium_menu = {7 : "Paua and Prawn Dumplings",8 : "Kina Canapes", 9 : "Kumara and Truffle Ravioli",10 : "Manuka Smoked Salmon", 11 : "Paua Porridge" }

all_orders = {}
valid_pc = ["0620", "0630", "0632"]
total_cost = 0
house_num = 0
street = ""
suburb = ""
phone = ""
order_num = 0
min_items = 3
budget_list_end = 6
prem_start = 7
prem_end = 11
deliver_cost =

def get_name():
    name = input("What is the name for the order?")
    print(budget_menu)
    print(premium_menu)







#I know there's magic numbers ill deal with them laters
def get_order():
    order_yn = input("Would you like to order?")
    while order_yn.lower() == "yes":
        ordered = []
        order_more = "yes"
        order_num = order_num + 1
        if order_more.lower() == "yes" :
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
        order_yn = input("would you like to place another order?")
        all_orders[order_num] = order1

print(all_orders)







