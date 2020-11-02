*** Settings ***
Library  SeleniumLirary

*** Variables ***
${Login url} http://localhost:8080/login.jsp
${Browser}  chorme


*** Keywords ***
Open Browser    ${Login url}    ${Browser}
Close Browser
    close all browers
OPen Login Page
    go to ${Login url}
Input username
    [Arguments] ${username}
    input username  id:your_name     ${username}
Input password
    [Arguments]  ${password}
    input password  id:your_pass    ${password}
click login button
    click element   xpath://*[@id="signin"]
Error message should be visible
    page should contain Login was unsuccessfull