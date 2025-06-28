import os
from datetime import datetime
import pytest
import chromedriver_autoinstaller  # 👈 Import this
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup(browser):
    # Automatically download and setup the correct chromedriver version
    chromedriver_autoinstaller.install()  # 👈 Auto matches Chrome version

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=chrome_options)  # 👈 No need for service
        print("Launching Chrome browser...")

    elif browser == "firefox":
        raise NotImplementedError("Firefox is not installed in the Docker image.")

    elif browser == "edge":
        raise NotImplementedError("Edge is not installed in the Docker image.")

    else:
        raise Exception(f"Browser not supported: {browser}")

    return driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use: chrome | firefox | edge"
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# ------------------- HTML Reporting -------------------

def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'Opencart'
        config._metadata['Module Name'] = 'CustRegistration'
        config._metadata['Tester'] = 'Ashish'

    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    config.option.htmlpath = os.path.join(reports_dir, f"{timestamp}.html")


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
