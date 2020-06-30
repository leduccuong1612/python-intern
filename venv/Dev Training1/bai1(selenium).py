from selenium import webdriver
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get(" http://192.168.100.222:8888/cartmigration_ui_ver3/public/")
driver.find_element_by_name("email").send_keys("test@test.com")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_css_selector('button.signin').click()
a = driver.find_element_by_id("navbarDropdown2").text
print(a)

