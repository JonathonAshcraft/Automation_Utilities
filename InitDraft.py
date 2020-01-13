# Obligatory Comment

# Selenium Test
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://cishoc.service-now.com/login_locate_sso.do")
driver.find_element_by_name("sso_selector_id").send_keys("jonathon.ashcraft@cognizant.com")
driver.find_element_by_name("not_important").click()





# driver.get("https://cishoc.service-now.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_cat_item_view.do%3Fv%3D1%26sysparm_id%3D67915990dbb16a409b3370e21f96190e%26sysparm_link_parent%3Ddc37adc1db31aa40851dfbec0f9619fc%26sysparm_catalog%3De0d08b13c3330100c8b837659bba8fb4%26sysparm_catalog_view%3Dcatalog_default%26sysparm_view%3Dcatalog_default")
# frame = driver.find_element_by_name('gsft_main')
# driver.switch_to.frame(frame)
# driver.find_element_("Use external login").click()