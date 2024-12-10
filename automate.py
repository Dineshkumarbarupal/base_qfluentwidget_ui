from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
 
class WaAutomate:
    def __init__(self):
        contact = "6377781395"
        text = "Hey, this message was sent using Selenium"

        chrome_option = Options()
        chrome_option.add_argument("--user-data-dir=C:\\Users\\NSG\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

        driver = webdriver.Chrome(options= chrome_option)
        driver.get("https://web.whatsapp.com")
        print("Scan QR Code:")
        # input("Press Enter to complete next task:")
        print("Logged In.")

        actions = ActionChains(driver)

        # Wait and locate the search box
        inp_xpath_search = '//*[@id="side"]/div[1]/div/div[2]/div[2]'
        input_box_search = WebDriverWait(driver, 50).until(
            Ec.element_to_be_clickable((By.XPATH, inp_xpath_search))
        )
        # input_box_search.click()
        actions.move_to_element(input_box_search).click().send_keys(contact).send_keys(Keys.ENTER).perform()
     
            # Use JavaScript to set value
            # driver.execute_script("arguments[0].innerText = arguments[1];", input_box_search, contact)
            # sleep(2)
            # input_box_search.send_keys(Keys.ENTER)  # Press Enter to search the contact
            # driver.execute_script("""
            # arguments[0].innerText = arguments[1];
            # arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            # """, input_box_search, contact)
            # sleep(1)
            # input_box_search.send_keys(Keys.ENTER)

        print("Contact entered successfully.")
        message_box = WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]')))
        actions.move_to_element(message_box).click().send_keys(text).send_keys(Keys.ENTER).perform()

        group = WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]')))
        actions.move_to_element(group).click().send_keys("BUSINESS ASSOCIATE").send_keys(Keys.ENTER).perform()


        print("This is the next line...")
        
        print("Mission successfull...")
        
if __name__== "__main__":
    WaAutomate()

    