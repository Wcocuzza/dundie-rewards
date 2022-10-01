from fileinput import filename
import os
import uuid
import pytest
from dundie.core import load
from .constants import PEOPLE_FILE

def setup_module():
    print("\nRoda antes dos testes desse modulo\n")


def teardown_module():
    print("\nRoda apos os testes desse modulo\n")

@pytest.fixture(scope='function', autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("TESTE")
    yield
    file_.remove()

@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test load function."""
    filename = f"arquivo_indesejado_{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filename))

    with open(filename, "w") as file_:
        file_.write("Dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'
