import csv
import checks

clean_rows = []
problem_rows = []

with open("customers_200.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for number, customer in enumerate(reader, start=1):
        messages = checks.check_customer(customer)
        number_of_messages = len(messages)
        customer_id = checks.get_text(customer, "customer_id")
        cleaned_name = checks.clean_name(checks.get_text(customer, "name"))
        cleaned_email = checks.clean_email(checks.get_text(customer, "email"))
        cleaned_phone = checks.clean_phone(checks.get_text(customer, "phone"))
        cleaned_city = checks.clean_city(checks.get_text(customer, "city"))
        if number_of_messages == 0:
            clean_rows.append({
                "customer_id": customer_id, 
                "name": cleaned_name, 
                "email": cleaned_email, 
                "phone": cleaned_phone, 
                "city": cleaned_city
            })
        else:
            problem_rows.append({
                "customer_id": customer_id, 
                "name": checks.get_text(customer, "name"), 
                "email": checks.get_text(customer, "email"), 
                "phone": checks.get_text(customer, "phone"), 
                "city": checks.get_text(customer, "city"),
                "problems": "; ".join(messages)
            })

with open("clean_customers.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["customer_id", "name", "email", "phone", "city"])
    writer.writeheader()
    writer.writerows(clean_rows)

with open("problems.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["customer_id", "name", "email", "phone", "city", "problems"])
    writer.writeheader()
    writer.writerows(problem_rows)