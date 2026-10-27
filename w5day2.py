import csv
import checks

groups = {}
rows = [("NW1", "ravi@gmail.com"), ("NW2", "meera@gmail.com"), ("NW3", "ravi@gmail.com")]

for customer_id, email in rows:
    # if email not in group:
    #   group[email] = []
    # group[email].append(customer_id)
    groups.setdefault(email, []).append(customer_id)

print(groups)

for email, ids in groups.items():
    if len(ids) > 1:
        print(f"{email}: {ids}")


custmer_by_city = {}
with open("customers_5000.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for customer in reader:
        city = checks.clean_city(customer["city"])
        custmer_by_city.setdefault(city, []).append(customer["customer_id"])

for city, ids in custmer_by_city.items():
    print(f"{city}: {len(ids)}")

print(sum(len(ids) for ids in custmer_by_city.values()))

custmer_by_email = {}
with open("customers_5000.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for customer in reader:
        email = checks.clean_email(customer["email"])
        custmer_by_email.setdefault(email, []).append(customer["customer_id"])

for email, ids in custmer_by_email.items():
    if len(ids) > 1:
        print(f"{email}: {len(ids)}")
print(max(len(ids) for ids in custmer_by_email.values()))


pairs = [("a", [1, 2, 3]), ("b", [1]), ("c", [1, 2])]
print(sorted(pairs, key=lambda item: len(item[1]), reverse=True))
