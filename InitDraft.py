# Obligatory Comment

# Selenium Test
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time


driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("http://tzgintranet.trizetto.com/SitePages/default.aspx")
driver.get("https://fedsso.trizetto.com/servicenow")
driver.get("https://cishoc.service-now.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_cat_item_view.do%3Fv%3D1%26sysparm_id%3D67915990dbb16a409b3370e21f96190e%26sysparm_link_parent%3Ddc37adc1db31aa40851dfbec0f9619fc%26sysparm_catalog%3De0d08b13c3330100c8b837659bba8fb4%26sysparm_catalog_view%3Dcatalog_default%26sysparm_view%3Dcatalog_default")
driver.switch_to_frame("gsft_main")
driver.find_element_by_name("ni.IO:4afa0ac2db69a6409b3370e21f961917")
driver.execute_script("console.log('fuckinfuckithey')")