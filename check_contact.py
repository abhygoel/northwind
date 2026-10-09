def clean_email(email):
    return email.strip().lower()

def clean_phone(phone):
    return phone.replace(" ", "").replace("-", "")

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

email = input("Customer email: ")
print(check_email(clean_email(email)))

phone = input("Customer phone: ")
print(check_phone(clean_phone(phone)))