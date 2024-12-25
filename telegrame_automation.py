from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TelegramAutomate:
    def __init__(self,contacts):
        self.contacts = contacts
        self.initialization()

    def initialization(self):
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=C:\\Users\\NSG\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("--profile-directory=profile 4")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://web.telegram.org")
        self.driver.maximize_window()

        sleep(4)

    def wait_for_element(self,xpath):

        return WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
            )

    def click_to_the_elements(self,xpath):

        element = self.wait_for_element(xpath)
        element.click()

    def send_keys_to_elements(self,xpath,keys):

        element = self.wait_for_element(xpath)
        element.send_keys(keys)
    
    def search_contacts(self):

        search_box_xpath = '//input[@placeholder="Search"]'

        self.click_to_the_elements(search_box_xpath)

        self.send_keys_to_elements(search_box_xpath,self.contacts)
        sleep(4)

if __name__ == '__main__':

    tel = TelegramAutomate("name")
    tel.search_contacts()


        

    
    