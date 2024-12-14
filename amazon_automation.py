from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep



class Amazon_automate:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.amazon.in')


        # options = Options()
        # options.add_argument("--ignore-certificate-errors")
        # self.sereach_product()



    def sereach_product(self):
        action = ActionChains(self.driver)

        # sereach_box_xpath = ''
        sereach = WebDriverWait(self.driver,12).until(Ec.element_to_be_clickable((By.XPATH,'//*[@id="twotabsearchtextbox"]')))

        action.move_to_element(sereach).click().perform()

  
sleep(2)
Amazon_automate()