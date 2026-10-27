import csv
import checks
from duplicates import DuplicateFinder

def show_groups(groups, names, limit=3):
    for key, ids in list(groups.items())[:limit]:
        members = []
        for customer_id in ids:
            members.append(f"{customer_id} {names[customer_id]}")
        print(f"{key}: {', '.join(members)}")

finder = DuplicateFinder()
with open("customers_5000.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for customer in reader:
        finder.add(checks.clean_customer(customer))

print(f"Total number of rows {finder.total_rows}")
print(f"No of extra copies {len(finder.copies())}")
print(f"No of records with a copy {len(set(finder.copies().values()))}")
email_groups = finder.same_email_groups()
print(f"Same email groups: {len(email_groups)}")
show_groups(email_groups, finder.names)
phone_groups = finder.shared_phone_groups()
print(f"Same phone groups: {len(phone_groups)}")
show_groups(phone_groups, finder.names)




