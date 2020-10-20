from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

browser = webdriver.Chrome(executable_path="./chromedriver.exe")
browser.get("http://localhost:8080/login.jsp")
# ActionChains(browser).click(browser.find_element_by_xpath("/html/body/nav/div/a[2]")).perform()

txtUser = browser.find_element_by_id("your_name")
txtUser.send_keys("leduchoaaaaaaaaaaaaa")

txtPassword = browser.find_element_by_id("your_pass")
txtPassword.send_keys("123456")

txtPassword.send_keys(Keys.ENTER)
