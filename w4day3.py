import checks

assert 2 + 2 == 4
# assert 2 + 2 == 5

assert checks.clean_name("  rAVI kumar") == "Ravi Kumar"
assert checks.check_name("AI") == "Name is too short"

result = checks.clean_phone("09876543210")
assert result == "9876543210", f"Got {result}"

def test_clean_phone_removes_leading_zero():
    assert checks.clean_phone("09876543210") == "9876543210"

def test_check_phone_rejects_first_digit_five():
    assert checks.check_phone("5876543210") == "Phone is invalid"

test_clean_phone_removes_leading_zero()
test_check_phone_rejects_first_digit_five()
print("All tests passed")