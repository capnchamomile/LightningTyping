from selenium import webdriver
from pyautogui import typewrite

speed_site = "https://typing-speed-test.aoeu.eu/?lang=en"

driver = webdriver.Firefox()
driver.get(speed_site)

currentword = str(driver.find_element_by_css_selector("span.currentword.currentword").text)

while currentword != '':
    typewrite(currentword + ' ', 0)
    currentword = str(driver.find_element_by_css_selector("span.currentword.currentword").text)
    
