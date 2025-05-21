budget_menu = {1 : "Kawakawa Spritzer",2 : "Pork and Puha Slider",3 : "Horopito Fish Collars",4 : "Kawakawa Muscles",5 : "Taro and Coconut Fritters",6 : "Kumara and Fennel Salad"}
premium_menu = {7 : "Paua and Prawn Dumplings",8 : "Kina Canapes", 9 : "Kumara and Truffle Ravioli",10 : "Manuka Smoked Salmon", 11 : "Paua Porridge" }
budget_price = 6
premium_price = budget_price * 1.5


name = input("What is the name for the order?")
print(budget_menu)
print(premium_menu)
ordered = []

#I know theres magic numbers ill deal with them laters
order_yn = input("Would you like to order?")
while  order_yn.lower() == "yes" or len(ordered) < 3:
    order_stuff = int(input("What would you like to order?"))
    if 1 <= order_stuff <= 6:
        ordered.append(budget_menu[int(order_stuff)])
        print(ordered)
    elif 7 <= order_stuff <= 11:
        ordered.append(premium_menu[int(order_stuff)])
        print(ordered)
    order_yn = input("Would you like to order?")

