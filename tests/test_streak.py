import pytest
from streak import longest_positive_streak

def test_empty():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_multiple_streaks_examples():
    # Provided example
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
    # Mixed with zeros and negatives; longest is three (3,4,5)
    assert longest_positive_streak([0, 1, 2, 0, 3, 4, 5, -2, 6]) == 3

def test_zeros_and_negatives_break_streak():
    assert longest_positive_streak([0, -1, 0, -5]) == 0
    assert longest_positive_streak([1, 2, 0, 3, -1, 4, 5, 6]) == 3

def test_single_values():
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([0]) == 0
    assert longest_positive_streak([-3]) == 0
