def clean_name(name):
    return name.strip().title()

def clean_email(email):
    return email.strip().lower()

def clean_phone(phone):
    return phone.replace(" ", "").replace("-", "")

def check_name(name):
    if len(name) == 0:
        return "Name is missing"
    elif len(name) < 3:
        return "Name is too short"
    else:
        return "Name is valid"

def check_email(email):
    if len(email) == 0:
        return "Email is missing"
    elif "@" not in email:
        return "Email is invalid"
    else:
        return "Email is valid"

def check_phone(phone):
    if len(phone) == 0:
        return "Phone is missing"
    elif len(phone) != 10 or (not phone.isdigit()):
        return "Phone is invalid"
    else:
        return "Phone is valid"

def is_valid(message):
    if message.endswith("is valid"):
        return True
    else:
        return False

customers = [
    {"name": "  rAVI kumar ", "email": " Ravi@Northwind.COM", "phone": "98765 43210"},
    {"name": "Al", "email": "al.northwind.com", "phone": "98765-43210"},
    {"name": "meera RAO", "email": "meera@northwind.com", "phone": "98765abcde"},
    {"name": "", "email": "", "phone": ""},
    {"name": "Sana Sheikh", "email": "sana@northwind.com", "phone": "9123456780"}
]

invalid_customers = 0

for number, customer in enumerate(customers, start=1):
    problems = 0
    cleaned_name = clean_name(customer["name"])
    result_name  = check_name(cleaned_name)
    is_valid_name = is_valid(result_name)
    cleaned_email = clean_email(customer["email"])
    result_email  = check_email(cleaned_email)
    is_valid_email = is_valid(result_email)
    cleaned_phone = clean_phone(customer["phone"])
    result_phone  = check_phone(cleaned_phone)
    is_valid_phone = is_valid(result_phone)
    if not is_valid_name:
        problems += 1
    if not is_valid_email:
        problems += 1
    if not is_valid_phone:
        problems += 1  
    if problems > 0:
        print(f"{number}. {cleaned_name}: {problems} problems")
        invalid_customers += 1
    else:
        print(f"{number}. {cleaned_name}: valid")

print(f"We have {len(customers) - invalid_customers} valid customers")
    