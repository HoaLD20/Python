import random
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager


class RegisterForm:
    @pytest.fixture()
    def setup(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        yield
        sleep(3)
        self.browser.close()

    def registerTest(self, setup):
        # for i in range(5):
        a = random.randint(5, 1000)
        self.browser.get("http://localhost:8080/signup.jsp")
        self.txtmail = self.browser.find_element_by_id("email").send_keys("leduchoa" + (str(a)) + "@gmail.com")

        self.txtfullname = self.browser.find_element_by_id("fullname").send_keys("le duc hoa")

        self.txtphone = self.browser.find_element_by_id("phone").send_keys("0912345678")

        self.txtpassword = self.browser.find_element_by_id("pass").send_keys("cH4eeeYccL4AWXy@")

        self.txtrepass = self.browser.find_element_by_id("re_pass").send_keys("cH4eeeYccL4AWXy@")

        self.browser.find_element_by_xpath("/html/body/section/div/div/div[1]/form/div[6]/div/label/span").click()

        self.browser.find_element_by_id("signup").click()
        self.alert = Alert(self.browser)
        self.alert.accept()
        assert self.browser.title == "test"