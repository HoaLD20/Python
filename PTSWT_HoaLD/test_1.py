from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import random
from threading import Thread
from selenium.webdriver.support.ui import WebDriverWait
import random
import decimal



""""
Le Duc Hoa CE140469

read user requirement
Submit script - excel - 20 bug least
Set 2
"""

s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards",
           "meows on", "flees from", "tries to automate", "explodes"]

"""
Genarate word
"""


def answermacker():
    return random.choice(s_verbs)


"""
gen dec
"""
def gendec():
    return decimal.Decimal(random.randrange(0, 999999999))

def genint():
    return random.randint(0, 999999999)


"""
random true answer
"""


def ranAns():
    return random.randint(1, 5)


"""
Setup before test
"""


def test_setup():
    global browser
    browser = webdriver.Chrome(ChromeDriverManager().install())


def test_100casewrong():
    for i in range(100):
        browser.get("http://localhost:8080/")

        value = answermacker()
        note = answermacker()

        browser.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/input[1]").send_keys(value)
        print(value)

        browser.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/input[2]").send_keys(note)
        print(note)

        browser.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/input[3]").submit()
        try:
            assert "Financial Management v2" in browser.title
        except:
            print("HTTP Status 500 – Internal Server Error")

def test_10casetrue():
    for i in range(100):
        browser.get("http://localhost:8080/")

        value = gendec()
        note = answermacker()

        browser.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/input[1]").send_keys(gendec())
        print(value)

        browser.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/input[2]").send_keys(note)
        print(note)

        WebDriverWait(browser, 5)

        browser.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/input[3]").submit()
        try:

            assert "Financial Management v2" in browser.title
        except:
            print("Wring in case " + i)

def test_100caseTrue():
    for i in range(100):
        browser.get("http://localhost:8080/")

        value = genint()
        note = answermacker()

        browser.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/input[1]").send_keys(value)
        print(value)

        browser.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/input[2]").send_keys(note)
        print(note)

        browser.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/input[3]").submit()
        try:
            assert "Financial Management v2" in browser.title
        except:
            print("HTTP Status 500 – Internal Server Error")



def test_close():
    browser.close()
    browser.quit()
