from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome() 
browser.get("http://10.201.12.67:8080/login.aspx") 



browser.find_element_by_id("txtUserName").send_keys("Test01") 
browser.find_element_by_id("txtUserPassword").send_keys("123456") 
browser.find_element_by_id("btnLogin").click() 



try:
    element = WebDriverWait(browser, 100).until(
         EC.presence_of_element_located((By.XPATH, '//*[@id="app-menu-placeholder-targetEl"]/div/img[@id="tool-1021-toolEl"]'))
    )
    print(element)
    element.click()
finally:
    print(1)

time.sleep(5)

try:
    element = WebDriverWait(browser, 100,0.5).until(
         EC.presence_of_element_located((By.XPATH, '//*[@id="app-menu-body"]/div/table/tbody/tr[1]/td[1]/div/span'))
    )
    element.click()
finally:
    print(1)
time.sleep(5)

try:
    element = WebDriverWait(browser, 100,0.5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app-menu-body"]/div/table/tbody/tr[3]/td[1]/div/span'))
    )
    element.click()
finally:
    print(1)

time.sleep(5)

try:
    element = WebDriverWait(browser, 100,0.5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app-menu-body"]/div/table/tbody/tr[4]/td[1]/div/span'))
    )
    element.click()
finally:
    print(1)

    EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[contains(@src,"sysmsg.aspx?menuid=110201")]'))
#browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'sysmsg.aspx?menuid=110201')]"))

time.sleep(5)


try:
    element = WebDriverWait(browser, 100,0.5).until(
        EC.presence_of_element_located((By.ID, 'tbSubject'))
    )
    element.click()
finally:
    print(1)

browser.switch_to.parent_frame()

time.sleep(5)

try:
    element = WebDriverWait(browser, 100,0.5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app-menu-body"]/div/table/tbody/tr[5]/td[1]/div/span'))
    )
    element.click()
finally:
    print(1)


# #browser.switch_to.frame(frame_reference=browser.find‌​_element_by_xpath(x‌‌​​path="//iframe[@id='frame_home']")) 

# browser.find_element_by_xpath('//*[@id="app-menu-placeholder-targetEl"]/div/img[@id="tool-1021-toolEl"]').click()
# time.sleep(5)
# browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody/tr[1]/td[1]/div/span').click()

# time.sleep(5)
# browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody/tr[3]/td[1]/div/span').click()

# time.sleep(5)
# browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody/tr[4]/td[1]/div/span').click()

# time.sleep(5)

# # browser.switch_to.frame(0)
# browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'sysmsg.aspx?menuid=110201')]"))

# browser.find_element_by_id("tbSubject").send_keys("1234")

# time.sleep(5)

# browser.switch_to.parent_frame()
# browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody/tr[5]/td[1]/div/span').click()




