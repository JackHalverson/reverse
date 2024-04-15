import pytest

from reverse_string import reverse_string

def test_reverse():
    a = reverse_string("Hello world")
    assert a == "dlrow olleH" 