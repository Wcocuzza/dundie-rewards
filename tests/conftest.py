import pytest

MARKER = """\
unit: Mark units tests
integration: Mark integration test
high: High Priority
medium: Medium Priority
low: Low Priority
"""

def pytest_configure(config):
    """Set a configuration in pyproject.toml"""
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)
def got_to_tmpdir(request):
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield