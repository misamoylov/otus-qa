import allure

from .steps import imported_step


@allure.step
def passing_step():
    pass


def test_with_step_in_fixture_from_conftest(fixture_with_conftest_step):
    passing_step()