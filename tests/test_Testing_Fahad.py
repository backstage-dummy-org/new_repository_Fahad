import pytest

from Testing_Fahad.Testing_Fahad import Testing_Fahad


def test_Testing_Fahad_positive_factorial():
    """TODO: replace"""
    try:
        assert Testing_Fahad(0) == 1
        assert Testing_Fahad(1) == 1
        assert Testing_Fahad(5) == 120
        assert Testing_Fahad(10) == 3628800
    except Exception as e:
        pytest.fail(str(e))


def test_Testing_Fahad_negative_factorial():
    """TODO: replace"""
    try:
        assert Testing_Fahad(-5) is None
        assert Testing_Fahad(-10) is None
    except Exception as e:
        pytest.fail(str(e))
