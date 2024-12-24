from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class TelegramAutomate:
    def __init__(self,contacts):
        self.contacts = contacts

    def initialization(self):
        self.driver = webdriver.Chrome()


    def wait_for_element(self,xpath):

        return WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
            )

    def click_to_the_elements(self,xpath):

        element = self.wait_for_element(xpath)
        element.click()

    def send_keys_to_elements(self,xpath):

        element = self.wait_for_element(xpath)
        element.send_keys(self.contacts)
    
    def search_contacts(self):

        search_box_xpath = ''





    
        

    
    