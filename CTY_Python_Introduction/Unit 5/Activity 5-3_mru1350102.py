#function
def calculate_total_price(product_price, quantity):
    return product_price * quantity
#input
product_name = input("What are you buying? ")
product_price = float(input("How much does the product cost per unit? "))
quantity = int(input("How many units of the product are you buying? "))

#FIRST METHOD

total_price = calculate_total_price(product_price, quantity)
print("The total price of %s %s is $%.2f" % (quantity, product_name, total_price))

#SECOND METHOD

#print("The total price of %s %s is $%.2f" % (quantity, product_name, calculate_total_price(product_price, quantity)))
 
