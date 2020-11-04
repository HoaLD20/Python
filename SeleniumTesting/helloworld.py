from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def test():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://vntesters.com")
    page_title = driver.title
    assert 'Cộng Đồng Kiểm Thử Phần Mềm' in page_title
    driver.quit()
