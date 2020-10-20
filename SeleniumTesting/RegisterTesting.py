from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

browser = webdriver.Chrome(executable_path="./chromedriver.exe")
browser.get("http://localhost:8080/")

for i in range(1000):
    browser.find_element_by_xpath("/html/body/nav/div/a[2]").click()
    browser.find_element_by_xpath("/html/body/div/section/div/div/div[2]/a").click()

    txtmail = browser.find_element_by_id("email")
    txtmail.send_keys("leduchoa"+i+"@gmail.com")

    txtfullname = browser.find_element_by_id("fullname")
    txtfullname.send_keys("lê đức hòa " + i)

    txtphone = browser.find_element_by_id("phone")
    txtphone.send_keys("0"+i+""+(i+1)+(i-1)+()+()+()+()+()+())


