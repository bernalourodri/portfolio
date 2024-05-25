import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

url = 'https://books.toscrape.com/'
driver.get(url)

titleElements = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]
stocks_list=[]

for title in titleElements:
	title.click()
	stock = int(driver.find_element(By.CLASS_NAME, "instock").text.replace('In stock (', '').replace(' available)', ''))
	stocks_list.append(stock)
	driver.back()

titleList = [title.get_attribute('title') for title in titleElements]

dictDF = {'title': titleList,
		  'stock': stocks_list}

df = pd.DataFrame(dictDF)

print(df)