def clean_name(name):
    return name.strip().title()

name = input("Customer name: ")
print(f"Welcome, {clean_name(name)}")