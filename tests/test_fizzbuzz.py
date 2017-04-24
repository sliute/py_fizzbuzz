from src.fizzbuzz import fizzbuzz

def test_fizzbuzz_3():
    assert fizzbuzz(3) == "fizz"

def test_fizzbuzz_5():
    assert fizzbuzz(5) == "buzz"

def test_fizzbuzz_15():
    assert fizzbuzz(15) == "fizzbuzz"

def test_fizzbuzz_nope():
    assert fizzbuzz(7) == 7
