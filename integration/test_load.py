import pytest
from subprocess import check_output, CalledProcessError


@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_command():
    """test command load"""
    out = check_output(
        ["dundie", "load", "integration/assets/people.csv"]
    ).decode("utf-8").split("\n")
    assert len(out) == 2

@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_command_with_wrong_params(wrong_command):
    """test command load"""
    with pytest.raises(CalledProcessError) as error:
        out = check_output(
            ["dundie", wrong_command, "integration/assets/people.csv"]
        ).decode("utf-8").split("\n")

    assert "status 2" in str(error.getrepr())
