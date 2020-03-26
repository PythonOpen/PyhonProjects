import time
from selenium import webdriver

# 通过keys键模拟键盘
from selenium.webdriver.common.keys import Keys

# 操作哪个浏览器就对哪个浏览器建一个实例
# 自动按照环境变量查找相应的浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
executable_path = "D:\chrome\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path)
# driver = webdriver.Chrome("D:\chrome\chromedriver\chromedriver.exe")

#  如果浏览器没有在相应的环境变量中，需要指定浏览器位置

driver.get("http://www.baidu.com")

# 通过函数查找title标签
print("Title: {0}".format(driver.title))

driver.quit()


