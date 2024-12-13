from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import csv
from time import sleep
 
class WaAutomate:
    def __init__(self,contact_detail,massage):
        self.contact_detail = contact_detail
        self.massage = massage
        # contact = "6377781395"
        # text = "Hey, this message was sent using Selenium"

        chrome_option = Options()
        chrome_option.add_argument("--user-data-dir=C:\\Users\\NSG\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

        driver = webdriver.Chrome()
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
        actions.move_to_element(input_box_search).click().send_keys(self.contact_detail).send_keys(Keys.ENTER).perform()
        try :
            print("Contact entered successfully.")
            message_box = WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]')))
            actions.move_to_element(message_box).click().send_keys(self.massage).send_keys(Keys.ENTER).perform()
        except Exception as e:
            print(f"an error occured{e}")

        group_profile = WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.XPATH,'//*[@id="main"]/header/div[2]/div[1]/div/span')))
        actions.move_to_element(group_profile).click().perform()

        contact_data = []
        contacts = driver.find_elements(By.XPATH, '//*[@id="pane-side"]/div/div/div/div[9]/div/div/div[2]/div[2]/div[2]/span[1]/span')  # Replace with actual contact element class
        # print(contacts.get_attribute("outerHTML"))
        for contact in contacts:
            try:
                name = contact.text  # Adjust XPATH based on the DOM structure
                print(name)
                contact_data.append({"Number": name})
            except Exception as e:
                print(f"Error extracting contact: {e}")

        # Step 4: Write to CSV
        csv_file = "contacts.csv"
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Number"])
            writer.writeheader()
            writer.writerows(contact_data)

        print(f"Data written to {csv_file}")

        # group = WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]')))
        # actions.move_to_element(group).click().send_keys("BUSINESS ASSOCIATE").send_keys(Keys.ENTER).perform()


        print("This is the next line...")
        
        print("Mission successfull...")
        
if __name__== "__main__":
    WaAutomate()

    