airports = {"IAD" : "Washington Dulles International, USA", "LHR" : "London Heathrow, UK", "NRT" : "Narita International, Japan", "MOW" : "Moscow Metropolitan Area, Russia", "SYD" : "Sydney International Airport, Australia"}
print(airports)
print(airports["LHR"])
for code, name in airports.items():
    print(code)
    print(name)
airports["MOW"] = "Moscow International Airport, Russia"
print(airports)
del(airports["NRT"])
print(airports)
print(len(airports))
airports["LAX"] = "Los Angeles International Airport, USA"
print(airports)
for code, name in airports.items():
    if code == "LHR":
        print(airports["LHR"])
    elif code == "YYC":
        print(airports["YYC"])
    else:
        print("Airport LHR or YYC not found")
    
