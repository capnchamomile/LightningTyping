from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui

speed_site = "https://typing-speed-test.aoeu.eu/?lang=en"

driver = webdriver.Firefox()
driver.get(speed_site)

currentword = str(driver.find_element_by_css_selector("span.currentword.currentword").text)

while currentword != '':
    pyautogui.typewrite(currentword + ' ', 0)
    print('Word  \'' + currentword + '\' typed into speed test')
    currentword = str(driver.find_element_by_css_selector("span.currentword.currentword").text)
