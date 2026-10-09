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

name  = input("Customer name: ")
email = input("Customer email: ")
phone = input("Customer phone: ")

name_result  = check_name(clean_name(name))
email_result = check_email(clean_email(email))
phone_result = check_phone(clean_phone(phone))

if is_valid(name_result) and is_valid(email_result) and is_valid(phone_result):
    print("Record is valid")
else:
    print("Record has problems:")
    if not is_valid(name_result):
        print(f"- {name_result}")
    if not is_valid(email_result):
        print(f"- {email_result}")
    if not is_valid(phone_result):
        print(f"- {phone_result}")