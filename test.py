from src import convert

def test_case_I():
    assert convert(1) == "I"
    assert convert(2) == "II"
    assert convert(3) == "III"
