from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WhatsAppAutomation:
    
    def __init__(self, driver, actions):
        self.driver = driver
        self.actions = actions
    
    def _wait_for_element(self, xpath, timeout=50):
        """
        Wait for an element to be clickable and return it.
        
        Args:
            xpath (str): The XPath of the element.
            timeout (int): The time to wait before throwing an exception.
        
        Returns:
            WebElement: The clickable element.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
    
    def _click_element(self, xpath):
        """
        Wait for the element and click it.
        
        Args:
            xpath (str): The XPath of the element to click.
        """
        element = self._wait_for_element(xpath)
        element.click()

    def _send_keys_to_element(self, xpath, text):
        """
        Wait for the input field, click it, and send the provided keys.
        
        Args:
            xpath (str): The XPath of the input field.
            text (str): The text to send to the input field.
        """
        element = self._wait_for_element(xpath)
        element.click()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def create_new_group(self):
        """
        Automate the process of creating a new group and adding members to it.
        """
        # Define XPaths for elements
        xpath_new_group_button = '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/span/div[2]/div/span'
        xpath_new_group_option = '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/span/div[2]/span/div/ul/li[1]/div'
        xpath_add_member_input = '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/div[2]/input'
        
        try:
            # Click on the "New Group" button
            self._click_element(xpath_new_group_button)
            
            # Select the "New Group" option
            self._click_element(xpath_new_group_option)
            
            # Add a member to the group
            self._send_keys_to_element(xpath_add_member_input, "ContactName")  # Replace with actual contact name

        except Exception as e:
            print(f"An error occurred: {e}")
