#Input for how much you scored
score = int(input("How many points did you score?"))
#Conditional Statement for ranking how much you scored
if score <= 200:
    print("You are a beginner")
elif score <= 500:
    print("You are advanced")
elif score > 500:
    print("You are an expert")
