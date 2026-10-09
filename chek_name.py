def clean_name(name):
    return name.strip().title()

def check_name(name):
    if len(name) == 0:
        return "Name is missing"
    elif len(name) < 3:
        return "Name is too short"
    else:
        return "Name is valid"

name = input("Customer name: ")
name = clean_name(name)
print(check_name(name))