import random
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


class RegisterForm:
    @pytest.fixture()
    def setup(self):
        self.browser = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.browser.maximize_window()
        yield
        sleep(3)
        self.browser.close()

    def testPage(self, setup):
        self.browser.get("http://localhost:8080/signup.jsp")

    def registerTest(self, setup):
        # for i in range(5):
        a = random.randint(5, 1000)
        self.browser.get("http://localhost:8080/signup.jsp")
        self.txtmail = self.browser.find_element_by_id("email")
        self.txtmail.send_keys("leduchoa" + (str(a)) + "@gmail.com")

        self.txtfullname = self.browser.find_element_by_id("fullname")
        self.txtfullname.send_keys("le duc hoa")

        self.txtphone = self.browser.find_element_by_id("phone")
        self.txtphone.send_keys("0912345678")

        self.txtpassword = self.browser.find_element_by_id("pass")
        self.txtpassword.send_keys("cH4eeeYccL4AWXy@")

        self.txtrepass = self.browser.find_element_by_id("re_pass")
        self.txtrepass.send_keys("cH4eeeYccL4AWXy@")

        self.browser.find_element_by_xpath("/html/body/section/div/div/div[1]/form/div[6]/div/label/span").click()

        # browser.find_element_by_id("signup").click()
        # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))).click()
        self.browser.find_element_by_id("signup").click()
        self.alert = Alert(self.browser)
        self.alert.accept()
