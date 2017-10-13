from selenium import webdriver 
import time
browser = webdriver.Chrome() 
browser.get("file:///C:/Users/Administrator/Desktop/%E7%99%BE%E5%BA%A6%E4%B8%80%E4%B8%8B%EF%BC%8C%E4%BD%A0%E5%B0%B1%E7%9F%A5%E9%81%93.html") 
# browser.find_element_by_id("kw").send_keys("selenium") 
# browser.find_element_by_id("su").click() 
print(browser.title)
browser.quit()
