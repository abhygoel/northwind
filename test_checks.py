import pytest
import checks

@pytest.mark.parametrize("email", [
    "ravi@gmail.com",
    "ravi.kumar@yahoo.co.in",
])
def test_check_email_accepts(email):
    assert checks.check_email(email) == "Email is valid"

@pytest.mark.parametrize("email", [
    "@outlook.com",
    "imran.das60@gmail,com",
    "ravi@@gmail.com",
    "abhisekgoel@gmailcom",
    "abhisek goel@gmail.com"

])
def test_check_email_rejects(email):
    assert checks.check_email(email) == "Email is invalid"

@pytest.mark.parametrize("phone", [
    "9876543210"
])
def test_check_phone_accepts(phone):
    assert checks.check_phone(phone) == "Phone is valid"

@pytest.mark.parametrize("phone", [
    "724363184",
    "5876543210",
    "9876543abc"
])
def test_check_phone_rejects(phone):
    assert checks.check_phone(phone) == "Phone is invalid"

def test_clean_name_remove_spaces():
    assert checks.clean_name("  ravi   ") == "Ravi"

def test_clean_email_to_lower():
    assert checks.clean_email("AbhishekGoel@GMAIL.Com") == "abhishekgoel@gmail.com"

def test_clean_city_to_title():
    assert checks.clean_city("hyderabad") == "Hyderabad"

def test_clean_phone_remove_spaces_and_dashes():
    assert checks.clean_phone(" 9876-543-210") == "9876543210"

def test_clean_phone_remove_plus91():
    assert checks.clean_phone("+919876543210") == "9876543210"

def test_clean_phone_remove_91():
    assert checks.clean_phone("919876543210") == "9876543210"

def test_clean_phone_remove_0_prefix():
    assert checks.clean_phone("09876543210") == "9876543210"

def test_clean_phone_remove_letters():
    assert checks.clean_phone("abcd9876543210") == "9876543210"

def test_check_name_valid():
    assert checks.check_name("Ravi Kumar") == "Name is valid"

def test_check_name_missing():
    assert checks.check_name("") == "Name is missing"

def test_check_name_too_short():
    assert checks.check_name("AI") == "Name is too short"

def test_check_name_digit():
    assert checks.check_name("Ravi123") == "Name is invalid"

def test_check_name_apostrophe():
    assert checks.check_name("D'Souza") == "Name is valid"

def test_check_email_missing():
    assert checks.check_email("") == "Email is missing"

def test_check_phone_missing():
    assert checks.check_phone("") == "Phone is missing"

def test_check_customer_valid():
    customer = {
        "name": "Ravi Kumar",
        "email": "ravi@northwind.com",
        "phone": "9876543210"
    }
    assert checks.check_customer(customer) == []

def test_check_customer_invalid():
    customer = {
        "name": "AI",
        "email": "ravi@northwind.com",
        "phone": "987654321"
    }
    assert checks.check_customer(customer) == ["Name is too short", "Phone is invalid"]

def test_clean_customer():
    customer = {
        "customer_id": "001",
        "name": "  rAVI kumar ",
        "email": "ravi@northwind.com",
        "phone": "9876543210",
        "city": "Hyderabad"
    }
    cleancustomer = {
            "customer_id": "001",
            "name": "Ravi Kumar",
            "email": "ravi@northwind.com",
            "phone": "9876543210",
            "city": "Hyderabad"
        }
    original = dict(customer)
    result = checks.clean_customer(customer)
    assert customer == original
    assert result == cleancustomer
