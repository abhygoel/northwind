names = ["Ravi", "Meera", "Arjun"]

for name in names:
    print(f"Hello, {name}")

orders = [1200, 450, 3000, 800]
big = 0
total = 0

for amount in orders:
    print(amount*1.18)
    total += amount
    if amount >= 1000:
        big = big + 1
    print(f"total orders {total}")
    
print(f"{big} big orders")


cities = [" pune", "MUMBAI", "delhi"]
clean = []

for city in cities:
    clean.append(city.strip().title())

print(clean)

for number, name in enumerate(names, start=1):
    print(f"{number}. {name}")