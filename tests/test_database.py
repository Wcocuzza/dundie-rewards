import pytest
from dundie.database import EMPTY_DB, connect, commit

@pytest.mark.unit
def test_database_schema():
  db = connect()
  assert db.keys() == EMPTY_DB.keys()


@pytest.mark.unit
def test_commit_to_database():
  db = connect()
  data = {
    "name": "Wallace Cocuzza",
    "role": "Developer",
    "dept": "System"
  }

  db["people"]["wallace@email.com"] = data
  commit(db)

  db = connect()
  assert db["people"]["wallace@email.com"] == data
