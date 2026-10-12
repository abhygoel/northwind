customer = {"name": "Kiran Reddy"}

print(customer.get("name",""))
print(customer.get("phone",""))

value = None
print(value is None)

phone = 9876543210
print(str(phone))
print(int("1200") + 100)

amount = input("Order amount: ")

try:
    amount = int(amount)
    print(f"With tax: {amount * 1.18}")
except ValueError:
    print("That isn't a number")

quantity = input("Order quantity: ")

try:
    quantity = int(quantity)
    print(f"With Double: {quantity * 2}")
except ValueError:
    print("This isn't a number")

dictionary = {}
print(dictionary.get("city","Unknown"))

value = value.strip()

