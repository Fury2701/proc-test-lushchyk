import sys
import os
from project.core import process

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_process_triples_values():
    assert process([1, 2, 3]) == [3, 6, 9]


def test_process_ignores_non_int():
    assert process([1, "a", 3]) == [3, 9]
