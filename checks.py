import re

NAME_PATTERN = r"[A-Za-z][A-Za-z .'-]+"
EMAIL_PATTERN = r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"
PHONE_PATTERN = r"[6-9]\d{9}"

def clean_name(name):
    return name.strip().title()

def clean_email(email):
    return email.strip().lower()

def clean_phone(phone):
    phone = re.sub(r"\D", "", phone)
    if len(phone) == 12 and phone.startswith("91"):
        return phone[2:]
    elif len(phone) == 11 and phone.startswith("0"):
        return phone[1:]
    else:
        return phone

def clean_city(city):
    return city.strip().title()

def clean_customer(customer):
    return {
        "customer_id": get_text(customer, "customer_id"),
        "name": clean_name(get_text(customer, "name")),
        "email": clean_email(get_text(customer, "email")),
        "phone": clean_phone(get_text(customer, "phone")),
        "city": clean_city(get_text(customer, "city"))
        }

def check_name(name):
    if len(name) == 0:
        return "Name is missing"
    elif len(name) < 3:
        return "Name is too short"
    elif not re.fullmatch(NAME_PATTERN, name):
        return "Name is invalid"
    else:
        return "Name is valid"

def check_email(email):
    if len(email) == 0:
        return "Email is missing"
    elif not re.fullmatch(EMAIL_PATTERN, email):
        return "Email is invalid"
    else:
        return "Email is valid"

def check_phone(phone):
    if len(phone) == 0:
        return "Phone is missing"
    elif not re.fullmatch(PHONE_PATTERN, phone):
        return "Phone is invalid"
    else:
        return "Phone is valid"

def is_valid(message):
    if message.endswith("is valid"):
        return True
    else:
        return False

def get_text(customer, key):
    value = customer.get(key, "")
    if value is None:
        return ""
    else:
        return str(value)

def check_customer(customer):
    messages = []
    result_name  = check_name(customer["name"])
    if not is_valid(result_name):
        messages.append(result_name)
    result_email  = check_email(customer["email"])
    if not is_valid(result_email):
        messages.append(result_email)
    result_phone  = check_phone(customer["phone"])
    if not is_valid(result_phone):
        messages.append(result_phone)
    return messages

def get_label(number, name, email):
    if len(name) == 0:
        if len(email) == 0:
            return f"Record {number}"
        else:
            return email
    else:
        return name