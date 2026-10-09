def greet():
    print("Welcome to Northwind Supplies")

greet()
greet()

def greet(name):
    print(f"Welcome, {name}")

greet("Ravi")
greet("Meera")

def full_label(name, city):
    return f"{name} ({city})"

label = full_label("Ravi", "Pune")
print(label)

messy = "   rAVI kumar   "
print(messy.strip())
print(messy.title())
print(messy.strip().title())



def shout(text):
    return text.upper()

print(shout("ravi"))

def add_tax(price):
    return price*1.18

print(add_tax(100))

