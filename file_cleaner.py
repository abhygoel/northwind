import csv
import checks
import os
from datetime import date
import argparse
from pathlib import Path
import time
from duplicates import DuplicateFinder

def clean_file(input_path, clean_path, problem_path, duplicate_path, review_path, summary_path):
    clean_rows = []
    problem_rows = []
    counts = {}
    details = {}
    summary_lines = []
    duplicate_rows = []
    review_rows = []
    finder = DuplicateFinder()

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} doesn't exist.")
    
    with open(input_path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for customer in reader:
            cleaned = checks.clean_customer(customer)
            finder.add(cleaned)
            customer_id = checks.get_text(customer, "customer_id")
            if customer_id in finder.copies():
                original_id = finder.copies()[customer_id]
                duplicate_rows.append({
                    "customer_id": customer_id,
                    "original_id": original_id,
                    "name": checks.get_text(customer, "name"), 
                    "email": checks.get_text(customer, "email"), 
                    "phone": checks.get_text(customer, "phone"), 
                    "city": checks.get_text(customer, "city")
                })
            else:
                messages = checks.check_customer(cleaned)
                number_of_messages = len(messages)
    
                for message in messages:
                    counts[message] = counts.get(message, 0) + 1
    
                if number_of_messages == 0:
                    clean_rows.append(cleaned)
                else:
                    problem_rows.append({
                        "customer_id": customer_id, 
                        "name": checks.get_text(customer, "name"), 
                        "email": checks.get_text(customer, "email"), 
                        "phone": checks.get_text(customer, "phone"), 
                        "city": checks.get_text(customer, "city"),
                        "problems": "; ".join(messages)
                    })
                details[cleaned["customer_id"]] = customer

    email_groups = finder.same_email_groups()
    for email, ids in email_groups.items():
        for customer_id in ids:
            customer = details[customer_id]
            review_rows.append({
                "group": email,
                "reason": "likely same person",
                "customer_id": customer_id,
                "name": checks.get_text(customer, "name"),
                "email": checks.get_text(customer, "email"),
                "phone": checks.get_text(customer, "phone"),
            })

    phone_groups = finder.shared_phone_groups()
    for phone, ids in phone_groups.items():
        for customer_id in ids:
            customer = details[customer_id]
            review_rows.append({
                "group": phone,
                "reason": "shared phone, check before merging",
                "customer_id": customer_id,
                "name": checks.get_text(customer, "name"),
                "email": checks.get_text(customer, "email"),
                "phone": checks.get_text(customer, "phone"),
            })

    summary_lines.append("Northwind customer data check")
    summary_lines.append(f"Run date: {date.today()}")
    summary_lines.append(f"Input file: {input_path}")
    summary_lines.append("")
    summary_lines.append(f"Records checked: {finder.total_rows}")
    summary_lines.append(f"Duplicates removed: {len(duplicate_rows)}")
    summary_lines.append(f"Review: likely same person: {len(email_groups)} groups")
    summary_lines.append(f"Review: shared phone: {len(phone_groups)} groups")
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

    with open(duplicate_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["customer_id", "original_id", "name", "email", "phone", "city"])
        writer.writeheader()
        writer.writerows(duplicate_rows)
    
    with open(review_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["group", "reason", "customer_id", "name", "email", "phone"])
        writer.writeheader()
        writer.writerows(review_rows)

    with open(summary_path, "w", encoding="utf-8") as file:
        file.write(summary)

    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean Northwind customer data.")
    parser.add_argument("input_file", help="the CSV export to clean")
    parser.add_argument("--output-dir", default=".", help="folder for the output files")
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    clean_path = output_dir / "clean_customers.csv"
    problem_path = output_dir / "problems.csv"
    duplicate_path = output_dir / "duplicates.csv"
    review_path = output_dir / "review.csv"
    summary_path = output_dir / "summary.txt"
    start = time.perf_counter()
    try:
        summary = clean_file(args.input_file, clean_path, problem_path, duplicate_path, review_path, summary_path)
    except FileNotFoundError as error:
        print(error)
    else:
        elapsed = time.perf_counter() - start
        print(summary)
        print(f"Finished in {elapsed:.2f} seconds")
                
    