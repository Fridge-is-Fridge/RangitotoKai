budget_menu = {1 : "Kawakawa Spritzer",2 : "Pork and Puha Slider",3 : "Horopito Fish Collars",4 : "Kawakawa Muscles",5 : "Taro and Coconut Fritters",6 : "Kumara and Fennel Salad"}
premium_menu = {1 : "Paua and Prawn Dumplings",2 : "Kina Canapes", 3 : "Kumara and Truffle Ravioli",4 : "Manuka Smoked Salmon", 5 : "Paua Porridge" }
budget_price = 6
premium_price = budget_price * 1.5


name = input("What is the name for the order?")
print(budget_menu)
print(premium_menu)

order_yn = input("Would you like to order?")
while  order_yn.lower() == "yes":
    order_stuff = input("What would you like to order?")
    ordered = []
    ordered.append(budget_menu[int(order_stuff)])
    order_yn = input("Would you like to order?")