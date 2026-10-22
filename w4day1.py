import re

print(re.fullmatch(r"\d{10}", "9876543210"))
print(re.fullmatch(r"\d{10}", "9876"))

if re.fullmatch(r"[6-9]\d{9}", "9876543210"):
    print("Looks like an Indian mobiel")

print(re.sub(r"\D", "", "+91 (98765) 43210"))

print(re.fullmatch(r"\d{6}", "500081"))
print(re.fullmatch(r"\d{6}", "50008"))
print(re.fullmatch(f"\d{6}", "5000811"))
print(re.fullmatch(r"C\d{4}", "C0001"))

print(re.search(r"\d","abcd"))
