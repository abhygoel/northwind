import csv
import checks

seen = set()
seen.add("ravi@gmail.com")
seen.add("meera@gmail.com")
seen.add("ravi@gmail.com")
print(seen)
print(len(seen))

if "ravi@gmail.com" in seen:
    print("Already seen")

emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "a@x.com"]
seen = set()
repeats = []

for email in emails:
    if email in seen:
        repeats.append(email)
    else:
        seen.add(email)

print(repeats)

row_key = ("Ravi Kumar", "ravi@gmail.com", "987654321", "Pune")
seen = set()
seen.add(row_key)
print(seen)
# seen.add(["a", "b"])

distinct_city = set()

with open("customers_5000.csv", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for customer in reader:
            clean_city = customer["city"]
            if not clean_city in distinct_city:
                    distinct_city.add(clean_city)
print(len(distinct_city))

