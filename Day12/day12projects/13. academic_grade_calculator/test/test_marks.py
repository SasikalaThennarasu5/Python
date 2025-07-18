import pytest
from gradesystem.marks import calculate_average
from gradesystem.exceptions import InvalidMarkError, EmptyMarksError

def test_valid_average():
    assert calculate_average([80, 90, 100]) == 90.0

def test_invalid_mark():
    with pytest.raises(InvalidMarkError):
        calculate_average([95, 110])

def test_empty_marks():
    with pytest.raises(EmptyMarksError):
        calculate_average([])
