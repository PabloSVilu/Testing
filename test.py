from src import convert

def test_case_I():
    assert convert(1) == "I"
    assert convert(2) == "II"
    assert convert(3) == "III"
    assert convert(4) == "IV"
    assert convert(10) == "X"
 

