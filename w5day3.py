import csv
import checks

class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

visits = Counter()
visits.add()
visits.add()
print(visits.count)

pune = Counter()
delhi = Counter()
pune.add()
print(pune.count, delhi.count)

class CityCounter:
    def __init__(self):
        self.by_city = {}

    def add(self, city):
        self.by_city[city] = self.by_city.get(city, 0) + 1

    def biggest(self):
        return max(self.by_city, key=self.by_city.get)


with open("customers_5000.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    city_counter = CityCounter()
    for customer in reader:
        city = checks.clean_city(customer["city"])
        city_counter.add(city)

print(city_counter.biggest())
print(city_counter.by_city)