from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path


def setup_driver():
    # set up the driver to access Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver