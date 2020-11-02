*** Settings ***
Library  Selenium
Resource  login_resource.robot
Suite Setup  Open Browser
Suite Teardown  Close Browser

*** Test Cases ***
create webdriver    chorme  executable_path="chormedriver.exe"
test1                   test            test
right login                   leduchoa9950@gmail.com 	61aa89e7e9ce9891774a517ee5eb512f

*** Keywords ***
Invalid login
    [Arguments]  ${username}    ${password}
    Input username  ${username}
    Input password  ${password}
    click login button