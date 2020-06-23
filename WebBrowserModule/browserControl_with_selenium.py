from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.facebook.com')
browser.maximize_window()
browser.implicitly_wait(2000)

username_text = browser.find_element_by_xpath("//input[@id='email']")
password_text = browser.find_element_by_xpath("//input[@id='pass']")
loginButton = browser.find_element_by_xpath("//input[@id='u_0_b']")

messenger_text = browser.find_element_by_xpath("//div[contains(text(),'Messenger')]")

username_text.send_keys('sohansghanti@hotmail.com')
password_text.send_keys("ROCKonSohan1)")

password_text.submit()
# loginButton.click()


browser.back()
browser.forward()
browser.refresh()


print(messenger_text.text)

browser.quit()

