import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from setuptools.command.test import test
from webdriver_manager.chrome import ChromeDriverManager
import secrets
import string
import names

"""
setup before testing
"""


def test_setup():
    global browser
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # browser.implicitly_wait(10)
    browser.maximize_window()


"""
genarate String password
"""


def genaratePass():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    return password
    # return password


"""
random phone number
return phone number 
"""


def phoneran():
    p = list('0000000000')
    p[0] = str(random.randint(1, 9))
    for i in [1, 2, 6, 7, 8]:
        p[i] = str(random.randint(0, 9))
    for i in [3, 4]:
        p[i] = str(random.randint(0, 8))
    if p[3] == p[4] == 0:
        p[5] = str(random.randint(1, 8))
    else:
        p[5] = str(random.randint(0, 8))
    n = range(10)
    if p[6] == p[7] == p[8]:
        n = (i for i in n if i != p[6])
    p[8] = str(random.choice(n))
    p = ''.join(p)
    return "09" + p[:1] + p[3:6] + p[6:]

"""
random email
"""


def emailRan():
    random_char = ''.join(random.choice(string.ascii_letters) for x in range(8))
    return random_char(7) + "@gmail.com"


"""

"""


def charRan():
    return random.choice(string.ascii_letters)


"""
start 100 case but rejected by user
"""


def test_100caseWrong():
    for i in range(0, 100):
        # browser.implicitly_wait(10)

        browser.get("http://localhost:8080/signup.jsp")

        # browser.implicitly_wait(10)
        a = random.randint(5, 9999)
        # email wrong
        browser.find_element_by_id("email").send_keys("leduchoa" + (str(a)) + "@gmail.com")
        # fullname wrong
        name = names.get_full_name()
        browser.find_element_by_id("fullname").send_keys(name)
        # phone number
        browser.find_element_by_id("phone").send_keys(phoneran())
        # genarate password
        password = genaratePass()
        browser.find_element_by_id("pass").send_keys(password + "@" + "#" + "1" + "a")

        browser.find_element_by_id("re_pass").send_keys(password + "@" + "#" + "1" + "a")
        browser.find_element_by_xpath("/html/body/section/div/div/div[1]/form/div[6]/div/label/span").click()
        sleep(1)

        browser.find_element_by_id("signup").click()
        Alert(browser).accept()
        """
        display all filed
        """
        # print(str(i) + " mail: " + "leduchoa" + (str(a)) + "@gmail.com")
        print(name)
        # print(phoneran())
        print(password)


"""
close connection
"""


def test_close():
    browser.close()
    browser.quit()
