product_name = input("What are you buying? ")
product_price = input("How much does the product cost? ")
quantity = input("How much of the product are you buying? ")
totalPrice = float(product_price) * int(quantity)
print("The total price is $%s" % totalPrice)

