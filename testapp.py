from app import calculate_tax

def test_high_salary_tax():
    assert calculate_tax(6000) == 600

def test_low_salary_tax():
    assert calculate_tax(4000) == 0
