import os
import pytest
import uuid
from dundie.core import load
from .constants import PEOPLE_FILE

@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("Isso é sujeira")
    yield
    file_.remove()

@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test load function"""
    filepath = f"arquivo_indesejado_{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))
    with open(filepath, "w") as file_:
        file_.write("Dados indesejados(Test Side effect)")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'w'
