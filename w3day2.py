import csv

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

with open("customers_200.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    customers = list(reader)
hyderabad_count = 0
for number, row in enumerate(customers, start=1):
    if number == 1:   
        print(row)
        print(row["phone"])
    if number <= 5:
        print(row["customer_id"])
        print(row["city"])
    if row["city"].strip().lower() == "hyderabad":
        hyderabad_count += 1
print(f"Number of hyderabad customer is: {hyderabad_count}")

valid_customer = 0
counts = {}
for number, customer in enumerate(customers, start=1):
    messages = check_customer(customer)
    for message in messages:
        counts[message] = counts.get(message, 0) + 1
    
    number_of_messages = len(messages)
    cleaned_name = clean_name(get_text(customer, "name"))
    cleaned_email = clean_email(get_text(customer, "email"))
    customer_id = get_text(customer, "customer_id")
    label = get_label(customer_id, cleaned_name, cleaned_email)
    if number_of_messages == 0:
        valid_customer += 1
    else:
        print(f"{customer_id} {label}: {', '.join(messages)}")

print("")
print(f"Checked {len(customers)} records: {valid_customer} valid, {len(customers) - valid_customer} with problems")
if len(counts) > 0:
    print("Problems by type:")
    for message, count in counts.items():
        print(f"- {message}: {count}")