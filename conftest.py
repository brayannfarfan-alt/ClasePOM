import pytest
from utils.helpers import get_driver
from pathlib import Path

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()



Path("screenshots").mkdir(exist_ok=True)


@pytest.hookimpl(hookwrapper=True) #HOOK
def pytest_runtest_makereport(item, call):

    # SETUP
    # CALL
    # Teardown

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            driver.save_screenshot(
                f"screenshots/{item.name}.png" #configuracion de como se va a llamar mi captura
            )