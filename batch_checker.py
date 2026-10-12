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

def get_text(customer, key):
    value = customer.get(key, "")
    if value is None:
        return ""
    else:
        return str(value)

def check_customer(customer):
    messages = []
    cleaned_name = clean_name(get_text(customer, "name"))
    result_name  = check_name(cleaned_name)
    if not is_valid(result_name):
        messages.append(result_name)
    cleaned_email = clean_email(get_text(customer, "email"))
    result_email  = check_email(cleaned_email)
    if not is_valid(result_email):
        messages.append(result_email)
    cleaned_phone = clean_phone(get_text(customer, "phone"))
    result_phone  = check_phone(cleaned_phone)
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

customers = [
    {"name": "  rAVI kumar ", "email": " Ravi@Northwind.COM", "phone": "98765 43210"},
    {"name": "Al", "email": "al.northwind.com", "phone": "98765-43210"},
    {"name": "meera RAO", "email": "meera@northwind.com", "phone": "98765abcde"},
    {"name": "", "email": "", "phone": ""},
    {"name": "Sana Sheikh", "email": "sana@northwind.com", "phone": "9123456780"},
    {"name": "Kiran Reddy", "email": "kiran@northwind.com"},
    {"name": "Priya Nair", "phone": 9876543210},
    {"email": "jo@northwind.com", "phone": "98765 43210"},
    {"name": None, "email": "vikram@northwind.com", "phone": "9123456780"},
    {"name": "ARJUN mehta ", "email": "arjun@northwind.com", "phone": "91234-56789"},
    {"name": "Divya Iyer", "email": "divya@NORTHWIND.com ", "phone": "912345678"},
    {"name": "  ", "email": "rohit@northwind.com", "phone": "9988776655"},
    {"name": "Fatima Khan", "email": "fatima@northwind.com", "phone": "99887 76655"},
    {"name": "Lakshmi Menon", "email": "lakshmi.northwind.com", "phone": "9876501234"},
    {"name": "Rahul Verma", "email": "rahul@northwind.com", "phone": None},
    {"name": "Neha Gupta", "email": "neha@northwind.com", "phone": "98765432100"},
    {"name": "Suresh Babu", "email": "suresh@northwind.com", "phone": "9000012345"},
    {"name": "Anil", "email": "anil@northwind.com", "phone": "9000054321"},
    {"phone": "9811122233"},
    {"name": "Pooja Desai", "email": "pooja@northwind.com", "phone": "98111 22233"}
]

valid_customer = 0
counts = {}

for number, customer in enumerate(customers, start=1):
    messages = check_customer(customer)
    for message in messages:
        counts[message] = counts.get(message, 0) + 1
    
    number_of_messages = len(messages)
    cleaned_name = clean_name(get_text(customer, "name"))
    cleaned_email = clean_email(get_text(customer, "email"))
    label = get_label(number, cleaned_name, cleaned_email)
    if number_of_messages == 0:
        print(f"{number}. {label}: valid")
        valid_customer += 1
    else:
        if number_of_messages == 1:
            print(f"{number}. {label}: 1 problem")
        else:
            print(f"{number}. {label}: {number_of_messages} problems")
        for message in messages:
            print(f"    - {message}")
    
print("")
print(f"Checked {len(customers)} records: {valid_customer} valid, {len(customers) - valid_customer} with problems")
if len(counts) > 0:
    print("Problems by type:")
    for message, count in counts.items():
        print(f"- {message}: {count}")