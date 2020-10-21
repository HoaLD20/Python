from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import string
import secrets
import names


def genaratePass():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    return password


def test_setup():
    global browser
    browser = webdriver.Chrome(ChromeDriverManager().install())


"""
read file pass and return username and pass
"""


def getUsPas():
    with open("pass.txt") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        # for i in range(len(content) - 1):
        #     print("username:" + content[i])
        #     print("pass: " + content[i + 1])
    f.close()
    return content


def test_start():
    for i in range(100):
        browser.get("http://localhost:8080/login.jsp")
        name = names.get_full_name()
        password = genaratePass()
        with open("pass.txt") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            # for i in range(len(content) - 1):
            #     print("username:" + content[i])
            #     print("pass: " + content[i + 1])
        f.close()

        txtUser = browser.find_element_by_id("your_name").send_keys()
        txtPassword = browser.find_element_by_id("your_pass").send_keys()



        browser.find_element_by_id("signin").click()
        print(str(i) + " " + name)
        print(password)
        print()


def test_close():
    browser.close()
    browser.quit()
