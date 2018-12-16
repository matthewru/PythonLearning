#function
def calculate_total_Price(product_name, product_price, quantity):
    print("Total price of %d %s is $%.2f" % (quantity, product_name, (product_price * quantity)))
#input
product_name = input("What are you buying? ")
product_price = float(input("How much does the product cost per unit? "))
quantity = int(input("How many units of the product are you buying? "))
#calling function
calculate_total_Price(product_name, product_price, quantity)
