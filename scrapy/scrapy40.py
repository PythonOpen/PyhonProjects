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

text = driver.find_element_by_id('wrapper').text
# 通过函数查找title标签
print(text)
print(driver.title)
driver.save_screenshot('index.png')

driver.find_element_by_id('kw').send_keys(u"大熊猫")

driver.find_element_by_id('su').click()

time.sleep(5)
driver.save_screenshot("daxiongmao.png")

# 获取当前页面的cookie
print(driver.get_cookies())

# 模拟输入两个按键 ctrl + a，全选
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
# ctrl+x,剪切
driver.find_element_by_id("kw").send_keys(u'航空母舰')
driver.save_screenshot("hangmu01.png")

driver.find_element_by_id('su').send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot("hangmu02.png")

# 清空输入端,clear
driver.find_element_by_id('kw').clear()
driver.save_screenshot("clear.png")

driver.quit()