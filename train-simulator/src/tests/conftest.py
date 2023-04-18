import pytest
from _pytest.monkeypatch import MonkeyPatch

@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname)