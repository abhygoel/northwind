def clean_name(name):
    return name.strip().title()

def check_name(name):
    if len(name) == 0:
        return "Name is missing"
    elif len(name) < 3:
        return "Name is too short"
    else:
        return "Name is valid"
    
names = ["  rAVI kumar ", "meera RAO", "Al", "", "  sana Sheikh",
         "ARJUN mehta ", "  ", "Kiran Reddy", "jo", "Priya Nair  "]

print(len(names))
print(clean_name(names[0]))
print(clean_name(names[-1]))
print(check_name(clean_name(names[2])))
print(check_name(clean_name(names[3])))
names.append("  vikram SINGH ")
print(len(names))
