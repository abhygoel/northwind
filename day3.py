customers = 5000
print(customers > 1000)
print(customers == 5000)
print(customers != 5000)

orders = 12

if orders > 10:
    print("Key Customer")
else:
    print("Regular Customer")

if orders > 50:
    print("Platinum")
elif orders > 10:
    print("Gold")
else:
    print("Standard")

name = "Ravi"
print(len(name))
print(len(""))


order_amount = int(input("Amount: "))
if order_amount >= 1000:
    print("Free Delivery")
else:
    print("Delivery charge applies")

city = input("Customer city: ")
if city == "Hyderabad":
    print("Local")
    print(city.lower())
else:
    print("Outstation")
