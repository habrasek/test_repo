print("Welcome to the House of Pies! Here are our pies:")

print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, \n(7) Buko, (8) Burek,  (9) Tamale, (10) Steak")

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko","Burek",  "Tamale", "Steak"]

order = int(input("Which pie number would you like? "))

print("Great! We'll have that " + pie_list[order -1] + " right out for you")

answer = "yes"

total_order = []

total_order.append(pie_list[order -1])

while answer == "yes":
    order2 = int(input("Which pie number would you like? "))

    print("Great! We'll have that " + pie_list[order2 -1] + " right out for you")

    total_order.append(pie_list[order2 -1])
    
    answer = input("Would you like to order another pie? ")

print(total_order)
