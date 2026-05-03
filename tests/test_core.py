import sys
sys.path.insert(0, '.')
from project.core import process

def test_process_doubles_values():
    assert process([1, 2, 3]) == [2, 4, 6]

def test_process_ignores_non_int():
    assert process([1, "a", 3]) == [2, 6]
