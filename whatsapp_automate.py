import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep

class WaAutomate:

    def __init__(self, contact_detail, message):
        self.contact_detail = contact_detail
        self.message = message
        self.driver = self._initialize_driver()
        self.actions = ActionChains(self.driver)
        self.previous_contacts = set()
        self.contact_data = []

    def _initialize_driver(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # This is  for running the chrome without gui
        chrome_options.add_argument("--user-data-dir=C:\\Users\\NSG\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("--profile-directory=Profile 4")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://web.whatsapp.com")
        print("Scan QR Code to log in.")
        return driver

    def search_contact(self):
        inp_xpath_search = '//*[@id="side"]/div[1]/div/div[2]/div[2]'
        click_contect_xpath = '//*[@id="main"]/header/div[2]'
        contects_data_xpath = '//*[@id="app"]/div/div[3]/div/div[5]/span/div/span/div/div/div/section/div[6]/div[2]/div[2]/div[2]/div/span/div'

        input_box_search = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, inp_xpath_search))
        )
        self.actions.move_to_element(input_box_search).click().send_keys(self.contact_detail).send_keys(Keys.ENTER).perform()

        contects = WebDriverWait(self.driver,50).until(
            EC.element_to_be_clickable((By.XPATH, click_contect_xpath))
        )
        self.actions.move_to_element(contects).click().perform()

        contects_data = WebDriverWait(self.driver,50).until(
            EC.element_to_be_clickable((By.XPATH, contects_data_xpath))
        )
        self.actions.move_to_element(contects_data).click().perform()

    def extract_contacts(self):
        iframe_xpath = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]'
        new_data = self.driver.find_elements(By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[6]/div/div/div[2]/div[1]/div/div/span')
        iframe = self.driver.find_element(By.XPATH, iframe_xpath)

        for _ in range(90):
            self.driver.execute_script("arguments[0].scrollTop += 600;", iframe)
            sleep(1)

            contacts = self.driver.find_elements(By.CLASS_NAME, '_ajzr')
            new_data_found = self._process_contacts(contacts,new_data)

            if not new_data_found:
                print("stopped axtrating data")
                break

        self._write_to_csv()

    def _process_contacts(self, contacts,next_contacts):
        new_data_found = False
        for contact in contacts:
            try:
                name = contact.text.strip()
                if name and name not in self.previous_contacts:
                    self.previous_contacts.add(name)
                    self.contact_data.append({"Number": name})
                    print(f"Extracted: {name}")
                    new_data_found = True
                for next_contact in next_contacts:
                    try:
                        name = next_contact.text.strip()
                        if name and name not in self.previous_contacts:
                            self.previous_contacts.add(name)
                            self.contact_data.append({"Number": name})
                            print(f"Extracted: {name}")
                            new_data_found = True
                         
                            break
                    except Exception as e:
                        print(f"Error extacting contacet: {e}")
            except Exception as e:
                print(f"Error extracting contact: {e}")
        return new_data_found
    
    def _write_to_csv(self):
        csv_file = "contacts.csv"
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Number"])
            writer.writeheader()
            writer.writerows(self.contact_data)
        print(f"Data written to {csv_file}")

    def create_new_group(self):
        
        # data_frame_xpath = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/header/div/div[1]/div/span'
        new_group_button_xpath = '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/span/div[2]/div/span'
        new_group_xpath = '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/span/div[2]/span/div/ul/li[1]/div'
        add_group_member_xpath = '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/div[2]/input'

        # exit = WebDriverWait(self.driver,50).until(
        #     EC.element_to_be_clickable((By.XPATH, data_frame_xpath))
        # )
        # self.actions.move_to_element(exit).click().perform()

        new_group_button = WebDriverWait(self.driver,50).until(
            EC.element_to_be_clickable((By.XPATH, new_group_button_xpath))
        )
        self.actions.move_to_element(new_group_button).click().perform()

        new_group = WebDriverWait(self.driver,50).until(
            EC.element_to_be_clickable((By.XPATH, new_group_xpath))
        )
        self.actions.move_to_element(new_group).click().perform()

        add_group_member = WebDriverWait(self.driver,50).until(
            EC.element_to_be_clickable((By.XPATH, add_group_member_xpath))
        )
        self.actions.move_to_element(add_group_member).click().send_keys().send_keys(Keys.ENTER).perform()


       
    def send_message(self):
        try:
            message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]'
            message_box = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, message_box_xpath))
            )
            self.actions.move_to_element(message_box).click().send_keys(self.message).send_keys(Keys.ENTER).perform()
            print("Message sent successfully.")
        except Exception as e:
            print(f"Error sending message: {e}")


        
    def run(self):
        try:
            self.search_contact()
            self.extract_contacts()
            # self.create_new_group()
            # self.send_message()
            print("Automation completed successfully.")
        except Exception as e:
            print(f"An error occurred during automation: {e}")
        finally:
            self.driver.quit()


if __name__ == "__main__":
    wa = WaAutomate("study", "Hello! This is an automated message.")
    wa.run()
