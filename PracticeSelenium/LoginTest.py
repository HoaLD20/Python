from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin:

    @pytest.fixture(scope=classmethod)
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        yield
        self.driver.close()

    def testHome(self, setup):
        txtcheck = self.driver.get("https://opensource-demo.orangehrmlive.com/")

        txtusername = self.driver.find_element_by_id("txtUsername").send_keys("Admin")

        txtpassword = self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        txtusername = self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        assert txtusername =="Admin"
        txtpassword = self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        assert txtpassword == "admin123"
        assert self.driver.title == "hihi"

