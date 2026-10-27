import pytest
import checks
import file_cleaner
import csv
from duplicates import DuplicateFinder

def test_clean_file_end_to_end(tmp_path):
    input_path = tmp_path / "input.csv"
    input_path.write_text(
        "customer_id,name,email,phone,city\n"
        "C1,  ravi kumar ,RAVI@gmail.com,98765 43210,pune\n"
        "C2,Ravi Kumar,ravi@gmail.com,9876543210,Pune\n"
        "C3,Hari Kumar,hari@gmail.com,9876543210,Pune\n"
        "C4,Ravi K,ravi@gmail.com,9876543211,Pune\n"
        "C5,Al,bad-email,123,Delhi\n",
        encoding="utf-8",
    )
    cleancustomer = {
        "customer_id": "C1",
        "name": "Ravi Kumar",
        "email": "ravi@gmail.com",
        "phone": "9876543210",
        "city": "Pune"
    }
    clean_path = tmp_path / "clean.csv"
    problem_path = tmp_path / "problems.csv"
    duplicate_path = tmp_path / "duplicate.csv"
    review_path = tmp_path / "review.csv"
    summary_path = tmp_path / "summary.txt"
    summary = file_cleaner.clean_file(input_path, clean_path, problem_path, duplicate_path, review_path, summary_path)

    with open(clean_path, encoding="utf-8", newline="") as file:
        clean_rows = list(csv.DictReader(file))

    with open(problem_path, encoding="utf-8", newline="") as file:
        problem_rows = list(csv.DictReader(file))

    with open(duplicate_path, encoding="utf-8", newline="") as file:
        duplicate_rows = list(csv.DictReader(file))

    with open(review_path, encoding="utf-8", newline="") as file:
        review_rows = list(csv.DictReader(file))

    review_set = set()
    for row in review_rows:
        review_set.add((row["customer_id"], row["reason"]))

    assert len(clean_rows) == 3
    assert clean_rows[0] == cleancustomer 
    assert len(problem_rows) == 1
    assert len(review_rows) == 4
    assert len(duplicate_rows) == 1
    assert problem_rows[0]["customer_id"] == "C5"
    assert problem_rows[0]["problems"] == "Name is too short; Email is invalid; Phone is invalid"
    assert duplicate_rows[0]["customer_id"] == "C2"
    assert duplicate_rows[0]["original_id"] == "C1"
    assert "Clean: 3" in summary
    assert "Need fixing: 1" in summary
    assert "Duplicates removed: 1" in summary
    assert "Review: likely same person: 1 groups" in summary
    assert "Review: shared phone: 1 groups" in summary
    assert ("C4", "likely same person") in review_set
    assert ("C3", "shared phone, check before merging") in review_set
    
def test_clean_file_missing_input(tmp_path):
    input_path = tmp_path / "missing.csv"
    clean_path = tmp_path / "clean.csv"
    problem_path = tmp_path / "problems.csv"
    duplicate_path = tmp_path / "duplicate.csv"
    review_path = tmp_path / "review.csv"
    summary_path = tmp_path / "summary.txt"

    with pytest.raises(FileNotFoundError, match="doesn't exist"):
        file_cleaner.clean_file(input_path, clean_path, problem_path, duplicate_path, review_path, summary_path)


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
    "9876543abc",
    "abcd"
])
def test_check_phone_rejects(phone):
    assert checks.check_phone(phone) == "Phone is invalid"

@pytest.mark.parametrize("phone", [
    "",
    "  "
])
def test_check_phone_missing(phone):
    assert checks.check_phone(checks.clean_phone(phone)) == "Phone is missing"

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

def test_clean_phone_dontremove_letters():
    assert checks.clean_phone("abcd") == "abcd"

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

def make_finder(customers):
    finder = DuplicateFinder()
    for customer in customers:
        finder.add(checks.clean_customer(customer))
    return finder

@pytest.fixture
def sheikh_family():
    return [
        {"customer_id": "NW1", "name": "Lakshmi Sheikh", "email": "lakshmi@x.com",
         "phone": "9876543210", "city": "Hyderabad"},
        {"customer_id": "NW2", "name": "L. Sheikh", "email": "lakshmi@x.com",
         "phone": "9876543210", "city": "Hyderabad"},
        {"customer_id": "NW3", "name": "Sana Sheikh", "email": "sana@x.com",
         "phone": "9876543210", "city": "Hyderabad"},
        {"customer_id": "NW4", "name": "  sana SHEIKH ", "email": "SANA@X.COM",
         "phone": "+91 98765 43210", "city": "hyderabad"},
    ]

def test_copies(sheikh_family):
    finder = make_finder(sheikh_family)
    assert finder.copies() == {"NW4": "NW3"}

def test_same_email_finds_lakshmi(sheikh_family):
    finder = make_finder(sheikh_family)
    assert finder.same_email_groups() == {"lakshmi@x.com": ["NW1", "NW2"]}

def test_shared_phone_includes_sana(sheikh_family):
    finder = make_finder(sheikh_family)
    assert finder.shared_phone_groups() == {"9876543210": ["NW1", "NW2", "NW3"]}

def test_shared_phone_same_email():
    customers = [
        {"customer_id": "NW1", "name": "Lakshmi Sheikh", "email": "lakshmi@x.com",
         "phone": "9876543210", "city": "Hyderabad"},
        {"customer_id": "NW2", "name": "L. Sheikh", "email": "lakshmi@x.com",
         "phone": "9876543210", "city": "Hyderabad"},
    ]
    finder = make_finder(customers)
    assert finder.shared_phone_groups() == {}

def test_same_email_blank_emailid():
    customers = [
        {"customer_id": "NW1", "name": "Lakshmi Sheikh", "email": "",
         "phone": "9876543210", "city": "Hyderabad"},
        {"customer_id": "NW2", "name": "L. Sheikh", "email": "",
         "phone": "9876543210", "city": "Hyderabad"},
    ]
    finder = make_finder(customers)
    assert finder.same_email_groups() == {}
    
