customer = {
    "name": "Ravi Kumar",
    "email": "ravi@northwind.com",
    "phone": "9876543210"
}

print(customer["name"])
print(customer["email"])

customer["city"] = "Pune"
customer["phone"] = "9123456780"
print(customer)

customers = [
    {"name": "Ravi Kumar", "email": "ravi@northwind.com"},
    {"name": "Meera Rao", "email": "meera@northwind.com"}
]

print(customers[0]["name"])

for customer in customers:
    print(f"{customer['name']}: {customer['email']}")

product = {
    "name": "Battery",
    "price": 2000,
    "stock": 10
}

print(f"Product: {product['name']} at ${product['price']} has {product['stock']} remaining quantities")

product["category"] = "Consumables"
product["stock"] -= 1
print(product)
