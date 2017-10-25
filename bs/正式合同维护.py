from selenium import webdriver 
import time
import datetime


browser = webdriver.Chrome() 
browser.get("http://10.201.12.67:8080/login.aspx") 

browser.find_element_by_id("txtUserName").send_keys("Test01") 
browser.find_element_by_id("txtUserPassword").send_keys("123456") 
browser.find_element_by_id("btnLogin").click() 



now = datetime.datetime.now()

nowStr =now.strftime('%Y-%m-%d %H:%M:%S')  

id = "11112222"

tenantCode = 1000001

sleepTime = 3



time.sleep(10)

browser.find_element_by_xpath('//*[@id="app-menu-placeholder-targetEl"]/div/img[@id="tool-1021-toolEl"]').click()
time.sleep(sleepTime)
browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody//div/span[text()="运营管理"]').click()

time.sleep(sleepTime)
browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody//div/span[text()="合同管理"]').click()

time.sleep(sleepTime)
browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody//div/span[text()="正式合同"]').click()

time.sleep(sleepTime)

browser.find_element_by_xpath('//*[@id="app-menu-body"]/div/table/tbody//div/span[text()="正式合同维护"]').click()

time.sleep(sleepTime)


#1.新增:正式合同明细

browser.find_element_by_xpath('//*[@id="app-tabs-body"]//div/a/span/span/span[text()=" 新增 "]').click()
 
time.sleep(sleepTime)

browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'settle/contract_v2.aspx?opmode=m&type=f&menuid=13130301')]"))

time.sleep(sleepTime)

browser.find_element_by_id("TabContainer1_tabContent_tbTenantCode").send_keys(tenantCode)

browser.find_element_by_id("TabContainer1_tabContent_tbDescription").click()

time.sleep(sleepTime)

browser.find_element_by_id("TabContainer1_tabContent_tbDescription").send_keys("chen.yafei test 001")

browser.find_element_by_id("TabContainer1_tabContent_ddlPropertyType").click()

browser.find_element_by_xpath("//*[@id='TabContainer1_tabContent_ddlPropertyType']/*[text()='单元']").click()


browser.find_element_by_id("TabContainer1_tabContent_ddlBuildingId").click()

browser.find_element_by_xpath("//*[@id='TabContainer1_tabContent_ddlBuildingId']/*[text()='石家庄店']").click()

#2.合同条款

time.sleep(sleepTime)

browser.find_element_by_id("__tab_TabContainer1_tabTerm").click()
#browser.find_element_by_xpath("//*[@id='TabContainer1_tabTerm_tab']//span[text()='合同条款']").click()
time.sleep(sleepTime)

#商场代码：0106 月固定金额
browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl02_tbChargeCode").click()
browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl02_gvSelectCharge_ctl04_lbNoSelect").click()
time.sleep(sleepTime)

browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl02_ddlStartDateType").click()
browser.find_element_by_xpath("//*[@id='TabContainer1_tabTerm_gvTermList_ctl02_ddlStartDateType']/*[text()='指定日期']").click()
time.sleep(sleepTime)
browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl02_tbAssignStartDate").send_keys(nowStr)
browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl02_tbFirstSettleDate").send_keys(nowStr)

browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl02_tbPeriodSegment").send_keys(1)
browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl02_tbPeriodMonthsSet").send_keys(11)


browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl02_ibGenTerm").click()
time.sleep(sleepTime)

browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl02_gvTerm_ctl02_tbRentAmount").send_keys(10000)

#add new
browser.find_element_by_xpath("//*[@id='TabContainer1_tabTerm_gvTermList']/tbody/tr[2]/td[2]/input").click()
time.sleep(10)

#商场代码：0105 固定金额
browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl03_tbChargeCode").click()
browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl03_gvSelectCharge_ctl03_lbNoSelect").click()
time.sleep(sleepTime)

browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl03_ddlStartDateType").click()
browser.find_element_by_xpath("//*[@id='TabContainer1_tabTerm_gvTermList_ctl03_ddlStartDateType']/*[text()='指定日期']").click()
time.sleep(sleepTime)
browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl03_tbAssignStartDate").send_keys(nowStr)
browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl03_tbFirstSettleDate").send_keys(nowStr)

browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl03_tbPeriodSegment").send_keys(1)
browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl03_tbPeriodMonthsSet").send_keys(11)


browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl03_ibGenTerm").click()
time.sleep(sleepTime)

browser.find_element_by_id("TabContainer1_tabTerm_gvTermList_ctl03_gvTerm_ctl02_tbFixCommiRate").send_keys(7)


#单元
browser.find_element_by_id("__tab_TabContainer1_tabProperty").click()
time.sleep(sleepTime)

browser.find_element_by_id("TabContainer1_tabProperty_gvProperty_ctl02_tbPropertyCode").click()
time.sleep(sleepTime)

browser.find_element_by_xpath("//*[@id='TabContainer1_tabProperty_gvProperty_ctl02_panelSelectProperty']/div/table/tbody/tr[2]/td[1]/a").click()
time.sleep(10)

browser.find_element_by_id("TabContainer1_tabProperty_gvPropertyDetail_ctl02_tbStoreName").send_keys("chen.yafei store")
browser.find_element_by_id("TabContainer1_tabProperty_gvPropertyDetail_ctl02_tbStoreAddress").send_keys("chen.yafei home")



browser.find_element_by_id("TabContainer1_tabProperty_gvPropertyDetail_ctl02_ddlTillType").click()
browser.find_element_by_xpath("//*[@id='TabContainer1_tabProperty_gvPropertyDetail_ctl02_ddlTillType']/*[text()='WAVEN_POS']").click()


#参考文档
browser.find_element_by_id("__tab_TabContainer1_tabDocument").click()
time.sleep(sleepTime)

browser.find_element_by_id("TabContainer1_tabDocument_fuRefDoc1").send_keys("C:\\Users\\Administrator\\Desktop\\1.jpeg")
time.sleep(sleepTime)
browser.find_element_by_id("TabContainer1_tabDocument_btnFileUpLoad1").click()
time.sleep(sleepTime)


browser.switch_to.parent_frame()

browser.find_element_by_xpath('//*[@id="app-tabs-body"]//div/a/span/span/span[text()=" 保存 "]').click()


t = browser.switch_to_alert()
t.accept()


