from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


# read excel file
df = pd.ExcelFile('Order Placement.xlsm').parse('11-12-2022') 
name=df['Stock Name'].tolist()
number=df['BSE / NSE Code'].tolist()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
action = ActionChains(driver)
wait = WebDriverWait(driver, 5)
driver.get('https://www.morningstar.in')
time.sleep(10)


for i in range(len(name)):
    print(str(name[i])+" -> "+str(number[i]))

    # Search and Enter
    # search_term = str(name[i])
    search_number = str(number[i])
    sbox = driver.find_element(by=By.XPATH, value='//input[@placeholder="Quote"]')
    sbox.send_keys(search_number)
    time.sleep(5)
    driver.find_element(by=By.XPATH, value="//div/strong[contains(text(),'"+search_number+"')]").click()
    # driver.find_element(by=By.XPATH, value="(.//div[@class='col-xs-12 stock-details']/strong)").click()
    time.sleep(10)


    # Extract rating
    rating = driver.find_element(by=By.XPATH, value="//div[contains(@class, 'mds-star-rating__sal mds-star-rating--large__sal')]").get_attribute("aria-label")

    # Extract the value of price/book
    price_pre_book = driver.find_element(by=By.XPATH, value="(.//ul[@class='small-block-grid-3 large-block-grid-4 sal-component-band-grid']/li)[10]//div[@class='dp-value']").text

    # Extract the value of price/cash flow
    price_pre_cash_flow = driver.find_element(by=By.XPATH, value="(.//ul[@class='sal-xsmall-block-grid-2 small-block-grid-4']/li)[2]//div[@class='dp-value']").text

    # Extract the value of price/sales
    price_pre_sales = driver.find_element(by=By.XPATH, value="(.//ul[@class='sal-xsmall-block-grid-2 small-block-grid-4']/li)[3]//div[@class='dp-value']").text

    # Extract the value of price/earnings
    price_pre_earnings = driver.find_element(by=By.XPATH, value="(.//ul[@class='sal-xsmall-block-grid-2 small-block-grid-4']/li)[4]//div[@class='dp-value']").text

    # Extract the value of EBITDA
    driver.find_element(by=By.XPATH, value="(.//a[@id='ctl00_ContentPlaceHolder1_ucNavigation_rptNavigation_ctl02_lnkTab'])").click()
    time.sleep(10)
    ebitda = driver.find_element(by=By.XPATH, value="(.//table[@class='sal-summary-section__table']/tbody/tr[4]/td[4])").text

    # Extract the value of fair value
    driver.find_element(by=By.XPATH, value="(.//a[@id='ctl00_ContentPlaceHolder1_ucNavigation_rptNavigation_ctl03_lnkTab'])").click()
    time.sleep(10)
    if(driver.find_element(by=By.XPATH, value="(.//div[@class='sal-columns sal-small-8 sal-medium-12 legend-items']/div)[1]//span").text == 'Fair Value'):
        fair_value = driver.find_element(by=By.XPATH, value="(.//div[@class='sal-columns sal-small-8 sal-medium-12 legend-items']/div)[1]//div[@class='legend-price']/span").text
    else:
        fair_value = driver.find_element(by=By.XPATH, value="(.//div[@class='sal-columns sal-small-8 sal-medium-12 legend-items']/div)[2]//div[@class='legend-price']/span").text

    # Extract the value of total yield of TTM
    total_yield_of_ttm = driver.find_element(by=By.XPATH, value="(.//table[@class='mds-table__sal mds-table--fixed-column__sal']/tbody/tr[5]/td[12])").text



    print('\n\n\n\nrating: ' + rating)
    print('price_pre_book: '+ price_pre_book)
    print('price_pre_cash_flow: '+ price_pre_cash_flow)
    print('price_pre_sales: '+ price_pre_sales)
    print('price_pre_earnings: '+ price_pre_earnings)
    print('ebitda: '+ ebitda)
    print('fair_value: '+ fair_value)
    print('total_yield_of_ttm: '+ total_yield_of_ttm)
    print('\n\n\n\n')


