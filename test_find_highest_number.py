import pytest
from highest_number_finder import HighestNumberFinder

def test_array_of_one_item_returns_this_item():
    # arrange
    numbers = [33]
    expectedResult = 33
    cut = HighestNumberFinder()

    # act 
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result