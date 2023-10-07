import pytest
from subprocess import check_output

@pytest.mark.integration
def test_load():
    """test command load"""
    out = check_output(
            ["dundie", "load", "tests/assets/people.csv"]
        ).decode("utf-8").split("\n")
    assert len(out) == 2
