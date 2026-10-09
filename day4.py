email = "ravi@northwind.com"
print("@" in email)
print("@" not in email)

orders = 12
city = "Pune"

if orders > 10 and city == "Pune":
    print("Key local customer")

if city == "Pune" or city == "Mumbai":
    print("Maharastra region")

print("9876543210".isdigit())
print("98765-43210".isdigit())

phone = "98765 43210"
print(phone.replace(" ",""))

email = input("Customer email: ")
hasAtTheRate = "@" in email
hasDot = "." in email
print(f"email contains @: {hasAtTheRate}")
print(f"email contains .: {hasDot}")

phone = input("Customer phone: ")
print(phone.replace(" ","").replace("-",""))

pincode = input("Customer pincode: ")
if pincode.isdigit() and len(pincode) == 6:
    print("Valid")
else:
    print("InValid")
