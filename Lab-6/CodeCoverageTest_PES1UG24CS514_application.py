
import pytest
from train_fare import base_fare, concession, tatkal_charge


# BASE FARE TEST CASES

def test_sleeper_fare():
    assert base_fare("SL", 500) == 500

def test_3a_fare():
    assert base_fare("3A", 100) == 200

def test_2a_fare():
    assert base_fare("2A", 100) == 300

def test_1a_fare():
    assert base_fare("1A", 100) == 500

def test_minimum_fare():
    assert base_fare("SL", 10) == 50

def test_invalid_class():
    with pytest.raises(ValueError):
        base_fare("AC", 500)

def test_invalid_distance():
    with pytest.raises(ValueError):
        base_fare("SL", 0)

def test_negative_distance():
    with pytest.raises(ValueError):
        base_fare("SL", -100)


# CONCESSION TEST CASES

def test_adult_no_concession():
    assert concession(30, "M", False) == 0

def test_tatkal_no_concession():
    assert concession(30, "M", True) == 0

def test_child_below_5():
    assert concession(3, "M", False) == 100

def test_child_between_5_and_12():
    assert concession(10, "M", False) == 50

def test_child_age_12():
    assert concession(12, "M", False) == 50

def test_senior_female():
    assert concession(65, "F", False) == 50

def test_senior_male():
    assert concession(65, "M", False) == 40

def test_age_60():
    assert concession(60, "M", False) == 40


# TATKAL CHARGE TEST CASES

def test_sleeper_tatkal_charge():
    assert tatkal_charge("SL", 500) == 100

def test_other_class_tatkal_charge():
    assert tatkal_charge("3A", 500) == 150

def test_minimum_tatkal_charge():
    assert tatkal_charge("3A", 100) == 100

def test_maximum_tatkal_charge():
    assert tatkal_charge("3A", 2000) == 400

def test_tatkal_charge_above_400():
    assert tatkal_charge("1A", 2000) == 400

def test_tatkal_charge_between_limits():
    assert tatkal_charge("SL", 2000) == 200
