from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
user = "Manoj"
driver = webdriver.Chrome()
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element((By.CSS_SELECTOR,"#name")).send_keys(user)
driver.find_element((By.ID,"alertbtn")).click()
alert = driver.switch_to.alert
alertText = alert.text
alert.accept()
assert user in alertText
driver.quit()