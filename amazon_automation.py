from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
from fake_useragent import UserAgent


class Amazon_automate:
    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.get('https://www.amazon.in/s?k=laptop&page=2&crid=35QJVAQ8FT948&qid=1735184477&sprefix=laptop%2Caps%2C314&ref=sr_pg_2')
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)

        ua = UserAgent()
        options = Options()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument(f"user-agent={ua.random}")
        # self.sereach_product()

    def wait_for_elements(self,xpath):
        return WebDriverWait(self.driver,30).until(
            Ec.element_to_be_clickable((By.XPATH,xpath))
        )
    
    def click_to_elements(self,xpath):
        search_button = self.wait_for_elements(xpath)
        search_button.click()

    def sereach_product(self):

        sereach_box_xpath = '//*[@id="twotabsearchtextbox"]'
        self.click_to_elements(sereach_box_xpath)
        # sereach = WebDriverWait(self.driver,12).until(Ec.element_to_be_clickable((By.XPATH,)))
        sleep(10)

    def extract_data(self):
        pass
    
sleep(2)
a = Amazon_automate()
a.sereach_product()

