from selenium import webdriver 
import time
browser = webdriver.Chrome() 
browser.get("http://10.201.12.67:8080/login.aspx") 

browser.find_element_by_id("txtUserName").send_keys("Test01") 
browser.find_element_by_id("txtUserPassword").send_keys("123456") 
browser.find_element_by_id("btnLogin").click() 


id = "11112222"

sleepTime = 3



time.sleep(10)

browser.find_element_by_xpath('//*[@id="app-menu-placeholder-targetEl"]/div/img[@id="tool-1021-toolEl"]').click()
time.sleep(sleepTime)
browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody//div/span[text()="系统管理"]').click()

time.sleep(sleepTime)
browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody//div/span[text()="用户管理"]').click()

time.sleep(sleepTime)
browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody//div/span[text()="用户资料维护"]').click()

time.sleep(sleepTime)

for index in range(0,2):
    browser.find_element_by_xpath('//*[@id="app-tabs-body"]//div/a/span/span/span[text()=" 新增 "]').click()
    #1.新增
    time.sleep(sleepTime)

    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'staff.aspx?opmode=m&menuid=110306')]"))

    time.sleep(sleepTime)

    browser.find_element_by_id("TabContainer1_tabDetail_tbStaffCode2").send_keys(int(id)+index)
    browser.find_element_by_id("TabContainer1_tabDetail_tbStaffName2").send_keys("肖新苗")
    browser.find_element_by_id("TabContainer1_tabDetail_tbPwd").send_keys("1234")

    browser.switch_to.parent_frame()

    time.sleep(sleepTime)

    browser.find_element_by_xpath('//*[@id="app-tabs-body"]//div/a/span/span/span[text()=" 保存 "]').click()

    time.sleep(sleepTime)
    browser.find_element_by_xpath('//*[@id="messagebox-1001"]//div/a[2]').click()
    time.sleep(sleepTime)
    browser.switch_to.parent_frame()





#2.查询
time.sleep(sleepTime)

browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'staff.aspx?opmode=m&menuid=110306')]"))

browser.find_element_by_id("__tab_TabContainer1_tabEnquiry").click()
#browser.find_element_by_id("TabContainer1_tabEnquiry_tbStaffCode").send_keys(id)
browser.find_element_by_id("TabContainer1_tabEnquiry_tbStaffName").send_keys("肖新苗")

browser.switch_to.parent_frame()
time.sleep(sleepTime)
browser.find_element_by_xpath('//*[@id="app-tabs-body"]//div/a/span/span/span[text()=" 查询 "]').click()

#3.删除
time.sleep(sleepTime)
browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'staff.aspx?opmode=m&menuid=110306')]"))
for index in range(0,2):
    time.sleep(sleepTime)
    browser.find_element_by_id("TabContainer1_tabEnquiry_gvStaff").find_element_by_xpath('//*[text()="'+str(int(id)+index)+'"]/../../td[1]/input').click()


time.sleep(sleepTime)
browser.switch_to.parent_frame()
time.sleep(sleepTime)
browser.find_element_by_xpath('//*[@id="app-tabs-body"]//div/a/span/span/span[text()=" 删除 "]').click()

time.sleep(sleepTime)

browser.find_element_by_xpath('//*[@id="messagebox-1001-toolbar"]//div/a[2]').click()
browser.switch_to.parent_frame()
