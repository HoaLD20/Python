# import random
# from time import sleep
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.alert import Alert
#
# browser = webdriver.Chrome(executable_path="./chromedriver.exe")
#
# for i in range(5):
#     a = random.randint(5, 1000)
#     browser.get("http://localhost:8080/signup.jsp")
#     txtmail = browser.find_element_by_id("email")
#     txtmail.send_keys("leduchoa" + (str(a)) + "@gmail.com")
#
#     txtfullname = browser.find_element_by_id("fullname")
#     txtfullname.send_keys("le duc hoa")
#
#     txtphone = browser.find_element_by_id("phone")
#     txtphone.send_keys("0912345678")
#
#     txtpassword = browser.find_element_by_id("pass")
#     txtpassword.send_keys("cH4eeeYccL4AWXy@")
#
#     txtrepass = browser.find_element_by_id("re_pass")
#     txtrepass.send_keys("cH4eeeYccL4AWXy@")
#
#     browser.find_element_by_xpath("/html/body/section/div/div/div[1]/form/div[6]/div/label/span").click()
#
#     # browser.find_element_by_id("signup").click()
#     # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))).click()
#     browser.find_element_by_id("signup").click()
#     alert = Alert(browser)
#     alert.accept()
#     browser.close()
