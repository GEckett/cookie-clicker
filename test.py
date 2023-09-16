from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#calling website

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

mine_cost = driver.find_element(By.XPATH, value='//*[@id="buyMine"]/b').text.split("- ")[1].split(",")
mine_cost_final = int(mine_cost[0] + mine_cost[1])
print(mine_cost_final)