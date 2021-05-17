"""Test canary."""

from python_project_template import ppt


def test_tautology():
    """This test canary always passes."""
    assert 2 + 2 == 4


def test_sum_of_two_integers():
    """Test the sum() function."""
    expected = 4
    actual = ppt.sum_of_two_integers(2, 2)
    assert actual == expected
