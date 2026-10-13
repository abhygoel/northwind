import greetings
from greetings import hello, goodbye
from datetime import date
import os

print(greetings.hello("Ravi"))
print(greetings.goodbye("Ravi"))
print(hello("Meera"))
print(goodbye("Meera"))

print(date.today())
print(os.path.exists("customers_200.csv"))

phone = "+919876543210"
print(phone.startswith("+91"))
print(phone[3:])

if not os.path.exists("customer_200.csv"):
    print("Customer_200.csv doesnt exist in this folder")

