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

SearchTextBox = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Quote"]')))
action.move_to_element(SearchTextBox).click().send_keys('HINDUSTAN UNILEVER LTD').perform()
SearchTextBox.send_keys(Keys.ENTER)
time.sleep(10)










# Opening page and logging in
# driver.get('https://www.morningstar.in/stocks/0p0000bp7x/bse-itc-ltd/overview.aspx')
# driver.find_element_by_id("username").send_keys('Your UserID')
# driver.find_element_by_id("password").send_keys('Your Password')
# driver.find_element_by_xpath('//button[text()="Sign in"]').click()

# # Search and Enter
# time.sleep(50)
# SearchTextBox = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Quote"]')))
# action.move_to_element(SearchTextBox).click().send_keys('HINDUSTAN UNILEVER LTD').perform()
# SearchTextBox.send_keys(Keys.ENTER)

# # Click on Jobs
# wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Jobs"]'))).click()

# # Clicking company filter
# company_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.XPATH, '//button[@aria-label="Company filter. Clicking this button displays all Company filter options."]')))
# company_button.click()

# # Send Accenture keyword in the inputbox
# # Please modify the xpath as per your understanding. Relative path
# wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Add a company"]'))).send_keys('Accenture')
# time.sleep(5)

# # Collect all the options
# All_selection = driver.find_elements_by_xpath(
#     "//span[contains(@class,'search-typeahead-v2__hit-text t-14 t-black')]")

# # Printing all the options
# for i in All_selection:
#     print(i.text)

# # Click on the first Option.
# All_selection[0].click()