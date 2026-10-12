def clean_name(name):
    return name.strip().title()

def check_name(name):
    if len(name) == 0:
        return "Name is missing"
    elif len(name) < 3:
        return "Name is too short"
    else:
        return "Name is valid"

def is_valid(message):
    if message.endswith("is valid"):
        return True
    else:
        return False
    
names = ["  rAVI kumar ", "meera RAO", "Al", "", "  sana Sheikh",
         "ARJUN mehta ", "  ", "Kiran Reddy", "jo", "Priya Nair  "]

valid_names = []

for number, name in enumerate(names, start=1):
    cleaned = clean_name(name)
    result = check_name(cleaned)
    print(f"{number}. {cleaned}: {result}")
    if is_valid(result):
        valid_names.append(cleaned)
    

print(f"{len(valid_names)} valid, {len(names) - len(valid_names)} with problems")
print(valid_names)


