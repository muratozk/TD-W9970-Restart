from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://192.168.1.1/")
time.sleep(2)

username = browser.find_element_by_xpath("//*[@id='userName']")
password = browser.find_element_by_xpath("//*[@id='pcPassword']")

# Entered default username and password
username.send_keys("admin")
password.send_keys("turktelekom")

# Catch login parameter
login = browser.find_element_by_xpath("//*[@id='loginBtn']")
login.click()

time.sleep(2)

# Password login after not change newer password
skip = browser.find_element_by_xpath("//*[@id='skipBtn']")

skip.click()
time.sleep(2)

# Find left side menu menu button
find = browser.find_element_by_xpath("//*[@id='menu_tools']")
find.click()

# Open it restart menu
baslat = browser.find_element_by_xpath("//*[@id='menu_restart']")
baslat.click()
time.sleep(2)

# Restart button click
ok = browser.find_element_by_xpath("//*[@id='button_reboot']")
ok.click()
time.sleep(2)

# Catch alert message
alert = browser.switch_to.alert
time.sleep(2)

# Allowed alert message
alert.accept() # or dismiss
time.sleep(5)

browser.close()