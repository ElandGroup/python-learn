from selenium import webdriver 
import time
browser = webdriver.Chrome() 
browser.get("http://10.201.12.67:8080/login.aspx") 



browser.find_element_by_id("txtUserName").send_keys("Test01") 
browser.find_element_by_id("txtUserPassword").send_keys("123456") 
browser.find_element_by_id("btnLogin").click() 



time.sleep(10)

#browser.switch_to.frame(frame_reference=browser.find‌​_element_by_xpath(x‌‌​​path="//iframe[@id='frame_home']")) 

browser.find_element_by_xpath('//*[@id="app-menu-placeholder-targetEl"]/div/img[@id="tool-1021-toolEl"]').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody/tr[1]/td[1]/div/span').click()

time.sleep(5)
browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody/tr[3]/td[1]/div/span').click()

time.sleep(5)
browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody/tr[4]/td[1]/div/span').click()

time.sleep(5)

# browser.switch_to.frame(0)
browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'sysmsg.aspx?menuid=110201')]"))

browser.find_element_by_id("tbSubject").send_keys("1234")

time.sleep(5)

browser.switch_to.parent_frame()
browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody/tr[5]/td[1]/div/span').click()







# browser.find_element_by_id("txtUserName").send_keys("Test01") 
# browser.find_element_by_id("txtUserPassword").send_keys("123456") 
# browser.find_element_by_id("btnLogin").click() 


# browser.find_element_by_id("tool-1021-toolEl").click()
# browser.find_element_by_id("ext-gen1261").click()


# browser.quit()


# To switch to the required frame, if found, in 20 seconds
#     WebDriverWait wait = new WebDriverWait(driver, 20);
#     wait.until(ExpectedConditions.frameToBeAvailableAndSwitchToIt(By.xpath("//frameset[contains(@id,'topFrameset')]/frame[4]")));

# //locating the input element
# driver.findElement(By.xpath("//input[@id='userName']"));


