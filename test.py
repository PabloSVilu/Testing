from src import convert

def test_roman_numerals():
    assert convert(1) == "I"
    assert convert(2) == "II"
    assert convert(3) == "III"
    assert convert(4) == "IV"
    assert convert(5) == "V"
    assert convert(6) == "VI"
    assert convert(9) == "IX"
    assert convert(10) == "X"
    assert convert(20) == "XX"
    assert convert(30) == "XXX"
    assert convert(100) == "C"
    assert convert(500) == "D"
    assert convert(1000) == "M"
    
 

