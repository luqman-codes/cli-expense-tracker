from src.app import total

def test_total_sum():
    expenses = [{"title": "Tea", "amount": 2.5}, {"title": "Bus", "amount": 3.0}]
    assert total(expenses) == 5.5
