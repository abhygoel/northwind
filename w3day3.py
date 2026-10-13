import csv

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Northwind Supplies\n")
    file.write("200 customers\n")

rows = [
    {"customer_id": "C0001", "name": "Ravi Kumar"},
    {"customer_id": "C0002", "name": "Meera Rao"}
]

with open("test.csv", "w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["customer_id", "name"])
    writer.writeheader()
    writer.writerows(rows)

