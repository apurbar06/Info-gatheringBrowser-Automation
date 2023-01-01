from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
action = ActionChains(driver)
wait = WebDriverWait(driver, 5)
driver.get('https://www.morningstar.in/stocks/0p0000bp7x/bse-itc-ltd/overview.aspx')
time.sleep(10)


# Search and Enter
search_term ='Hindustan Unilever Ltd'
search_number = '500696'
sbox = driver.find_element(by=By.XPATH, value='//input[@placeholder="Quote"]')
sbox.send_keys(search_term)
time.sleep(5)
driver.find_element(by=By.XPATH, value="//div[contains(text(),'"+search_number+"')]").click()
time.sleep(10)


# Extract rating
rating = driver.find_element(by=By.XPATH, value="//div[contains(@class, 'mds-star-rating__sal mds-star-rating--large__sal')]").get_attribute("aria-label")


# Extract the value of price/book
price_pre_book = driver.find_element(by=By.XPATH, value="(.//ul[@class='small-block-grid-3 large-block-grid-4 sal-component-band-grid']/li)[10]//div[@class='dp-value']").text

    


print()
print()
print()
print()
print('rating: ' + rating)
print('price_pre_book: '+ price_pre_book)
print()
print()
print()
print()




