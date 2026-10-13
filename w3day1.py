with open("customers_200.csv", encoding="utf-8") as file:
    text = file.read()

print(text[:300])

with open("customers_200.csv", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

line = "C0001,IMRAN SHEIKH,imran@northwind.com,69600 13389,Bengaluru"
parts = line.split(",")
print(parts)
print(parts[1])

with open("customers_200.csv", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        if number <=5:
            print(line.strip())
        else:
            break

with open("customers_200.csv", encoding="utf-8") as file:
    columns = file.readline().strip().split(",")
    print(columns)

rows_with_91 = 0
number_of_customers = 0
total_lines = 0
columns = []
with open("customers_200.csv", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        total_lines = number
        if number == 1:
            columns = line.strip().split(",")
        else:
            number_of_customers += 1
            customer = line.strip().split(',')
            phone = customer[3].strip()
            if phone.startswith("+91"):
                rows_with_91 += 1

print(f"Total number of lines: {total_lines}, number of customers: {number_of_customers}")
print(columns)
print(f"Number of rows have phone starting with +91: {rows_with_91}")
