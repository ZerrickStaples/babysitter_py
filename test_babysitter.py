from babysitter import *

def test_calculate_hours():
    assert calculate_hours(17, 18) == 1

def test_earliest_start_time():
    assert calculate_hours(16, 18) == 1