import re

print(re.fullmatch(r"[a-z0-9]+", "ravi42"))
print(re.fullmatch(r"[a-z0-9._-]+", "3ravi.k_2"))
print(re.fullmatch(r"[a-z0-9]+", "ravi kumar"))

print(re.fullmatch(r"gmail.com", "gmail,com"))
print(re.fullmatch(r"gmail\.com", "gmail,com"))

print(re.search(r"\d", "Ravi2 kumar"))

print(re.fullmatch(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", "ravi@gmail.com"))
print(re.fullmatch(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", "ravi@gmail"))
print(re.fullmatch(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", "ravi@@gmail.com"))
print(re.fullmatch(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", "@gmail.com"))
print(re.fullmatch(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", "ravi.kumar@yahoo.co.in"))

print(re.fullmatch(r"[A-Za-z][A-Za-z .'-]+", "Ravi Kumar"))
print(re.fullmatch(r"[A-Za-z][A-Za-z .'-]+", "Mary D'Souza"))
print(re.fullmatch(r"[A-Za-z][A-Za-z .'-]+", "Anne-Marie"))
print(re.fullmatch(r"[A-Za-z][A-Za-z .'-]+", "A. Kumar"))
print(re.fullmatch(r"[A-Za-z][A-Za-z .'-]+", "R4vi Kumar"))
print(re.fullmatch(r"[A-Za-z][A-Za-z .'-]+", ".Ravi"))
