import platform
import pytest


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.122.244/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('allure')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional allure on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra


@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, environment_info):
    request.config._metadata.update(
        {"browser": request.config.getoption("--browser"),
         "address": request.config.getoption("--address")})
    yield


@pytest.fixture(scope="session")
def environment_info():
    os_platform = platform.platform()
    linux_dist = platform.linux_distribution()
    return os_platform, linux_dist


