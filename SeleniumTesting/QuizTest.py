import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from setuptools.command.test import test
from webdriver_manager.chrome import ChromeDriverManager
import secrets
import string
import names


def test_setup():
    global browser
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # browser.implicitly_wait(10)
    browser.maximize_window()


def test_100caseWrong():
    for i in range(0, 100):
        browser.get("http://localhost:8080/signup.jsp")