import csv
import checks
import os
import sys
from datetime import date

input_file = "customers_200.csv"
clean_file = "clean_customers.csv"
problem_file = "problems.csv"
summary_file = "summary.txt"
clean_rows = []
problem_rows = []
counts = {}
summary_lines = []


if not os.path.exists(input_file):
    print(f"Input file {input_file} doesn't exist.")
    sys.exit()

with open(input_file, encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for customer in reader:
        cleaned = checks.clean_customer(customer)
        messages = checks.check_customer(cleaned)
        number_of_messages = len(messages)

        for message in messages:
            counts[message] = counts.get(message, 0) + 1

        
        if number_of_messages == 0:
            clean_rows.append(cleaned)
        else:
            problem_rows.append({
                "customer_id": checks.get_text(customer, "customer_id"), 
                "name": checks.get_text(customer, "name"), 
                "email": checks.get_text(customer, "email"), 
                "phone": checks.get_text(customer, "phone"), 
                "city": checks.get_text(customer, "city"),
                "problems": "; ".join(messages)
            })

summary_lines.append("Northwind customer data check")
summary_lines.append(f"Run date: {date.today()}")
summary_lines.append(f"Input file: {input_file}")
summary_lines.append("")
summary_lines.append(f"Records checked: {len(clean_rows) + len(problem_rows)}")
summary_lines.append(f"Clean: {len(clean_rows)}")
summary_lines.append(f"Need fixing: {len(problem_rows)}")
if len(counts) > 0:
    summary_lines.append("")
    summary_lines.append("Problems by type:")
    for message, count in counts.items():
        summary_lines.append(f"- {message}: {count}")

summary = "\n".join(summary_lines)

with open(clean_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["customer_id", "name", "email", "phone", "city"])
    writer.writeheader()
    writer.writerows(clean_rows)

with open(problem_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["customer_id", "name", "email", "phone", "city", "problems"])
    writer.writeheader()
    writer.writerows(problem_rows)

with open(summary_file, "w", encoding="utf-8") as file:
    file.write(summary)

print(summary)