from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#calling website

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

#upgrade costs

cursor_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyCursor"]/b').text.split("-")[1])
gran_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]/b').text.split("-")[1])
factory_cost = int(driver.find_element(By.XPATH, value='//*[@id="buyFactory"]/b').text.split("-")[1])
mine_cost = driver.find_element(By.XPATH, value='//*[@id="buyMine"]/b').text.split("- ")[1].split(",")
mine_cost_final = int(mine_cost[0] + mine_cost[1])
ship_cost = driver.find_element(By.XPATH, value='//*[@id="buyShipment"]/b').text.split("- ")[1].split(",")
ship_cost_final = int(ship_cost[0] + ship_cost[1])
alchemy_cost = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b').text.split("-")[1].split(",")
alchemy_cost_final = int(alchemy_cost[0] + alchemy_cost[1])
portal_cost = driver.find_element(By.XPATH, value='//*[@id="buyPortal"]/b').text.split("-")[1].split(",")
portal_cost_final = int(portal_cost[0] + portal_cost[1] + portal_cost[2])
time_cost = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b').text.split("-")[1].split(",")
time_cost_final = int(time_cost[0] + time_cost[1] + time_cost[2])

#functions

def click():
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()

def upgrade(cookie_count):
    if cursor_cost <= cookie_count < gran_cost:
        buy_cursor = driver.find_element(By.ID, value="buyCursor")
        buy_cursor.click()
    elif gran_cost <= cookie_count < factory_cost:
        buy_gran = driver.find_element(By.ID, value="buyGrandma")
        buy_gran.click()
    elif factory_cost <= cookie_count < mine_cost_final:
        buy_factory = driver.find_element(By.ID, value="buyFactory")
        buy_factory.click()
    elif mine_cost_final <= cookie_count < ship_cost_final:
        buy_mine = driver.find_element(By.ID, value="buyMine")
        buy_mine.click()
    elif ship_cost_final <= cookie_count < alchemy_cost_final:
        buy_ship = driver.find_element(By.ID, value="buyShipment")
        buy_ship.click()
    elif alchemy_cost_final <= cookie_count < portal_cost_final:
        buy_alchemy = driver.find_element(By.ID, value="buyAlchemy")
        buy_alchemy.click()
    elif portal_cost_final <= cookie_count < time_cost_final:
        buy_portal = driver.find_element(By.ID, value="buyPortal")
        buy_portal.click()
    elif time_cost_final < cookie_count:
        buy_time = driver.find_element(By.ID, value="buyTime machine")
        buy_time.click()


#constants

game_on = True
timeout = time.time() + 60*5

while game_on:
    click()
    if time.time() > timeout:
        cps = driver.find_element(By.ID, value="cps").text
        print(cps)
        break
    else:
        cookie_count = int(driver.find_element(By.ID, value="money").text)
        upgrade(cookie_count)
