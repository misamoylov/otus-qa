import pytest


@pytest.mark.env("stage1")
def test_basic_db_operation():
    pass

# pytest -E stage2
# pytest -E stage1
