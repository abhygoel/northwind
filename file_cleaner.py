import csv
import checks
import os
from datetime import date

def clean_file(input_path, clean_path, problem_path, summary_path):
    clean_rows = []
    problem_rows = []
    counts = {}
    summary_lines = []

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} doesn't exist.")

    with open(input_path, encoding="utf-8", newline="") as file:
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
    summary_lines.append(f"Input file: {input_path}")
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

    with open(clean_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["customer_id", "name", "email", "phone", "city"])
        writer.writeheader()
        writer.writerows(clean_rows)

    with open(problem_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["customer_id", "name", "email", "phone", "city", "problems"])
        writer.writeheader()
        writer.writerows(problem_rows)

    with open(summary_path, "w", encoding="utf-8") as file:
        file.write(summary)

    return summary


if __name__ == "__main__":
    try:
        summary = clean_file("customers_week4.csv", "clean_customers.csv", "problems.csv", "summary.txt")
        print(summary)
    except FileNotFoundError as error:
        print(error)
    