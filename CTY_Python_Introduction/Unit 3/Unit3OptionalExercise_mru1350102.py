#Present value
car_price = 35000.00
#years used to pay for loan
total_years = 5
#years converted into months
total_months = total_years * 12
#annual interest rate
annual_interest_rate = 0.05
#monthly interest rate
monthly_interest_rate = annual_interest_rate / 12

#Monthly payment calculation
monthly_payment = (monthly_interest_rate * (car_price)) / (1 - (1 + monthly_interest_rate)**-total_months)

#Display using String Formatting
print("Purchase Price: $%d" % car_price)
print("Annual Interest Rate: %d percent" % (annual_interest_rate * 100))
print("Years To Pay Off: %d years" % total_years)
print("Monthly Payment: $%.2f" % monthly_payment)
