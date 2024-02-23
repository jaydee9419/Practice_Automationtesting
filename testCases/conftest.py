import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver
@pytest.fixture()
def setup2():
    options = Options()
    options.add_experimental_option('prefs', {'profile.managed_default_content_settings.javascript': 2})

    driver = webdriver.Chrome(options=options)
    return driver


