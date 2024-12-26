from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

# Configure browser options
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.90 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

# Open Amazon
driver.get("https://www.amazon.in")

# Simulate user activity
time.sleep(random.uniform(2, 5))  # Add random delay
search_box = driver.find_element("id", "twotabsearchtextbox")
search_box.send_keys("laptops")
search_box.submit()

# Extract data
time.sleep(random.uniform(2, 5))
products = driver.find_elements("css selector", "div.s-main-slot div[data-component-type='s-search-result']")
print(products)
for product in products[:5]:  # Scrape top 5 results
    title = product.find_element("css selector", "span.a-size-medium").text
    price = product.find_element("css selector", "span.a-price-whole").text if product.find_elements("css selector", "span.a-price-whole") else "Price not available"
    print(f"Product: {title}, Price: {price}")

driver.quit()
