import time, random, csv
from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



"""
install python:				https://www.python.org/downloads/
--> Custom installation --> Add to Path

install selenium:
pip install selenium

download edge webdriver from
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
keep the edge webdriver file in same folder as this file
"""


chrome_options = webdriver.ChromeOptions()
s=service.Service('chromedriver.exe')

l_abt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
log = []
unm = "veer_0909"
pwd = "VAM#090905"
browser = webdriver.Chrome(service = s, options = chrome_options)
browser.maximize_window()
browser.get("https://www.instagram.com")
time.sleep(2)
uname = browser.find_element("xpath", "//input[@type = 'text']")
uname.send_keys(unm)
paswd = browser.find_element("xpath", "//input[@type = 'password']")
paswd.send_keys(pwd)
submit = browser.find_element("xpath", "//button[@type = 'submit']")
submit.click()
time.sleep(5)

l_following, l_followers = [],[]

browser.get("https://www.instagram.com/"+unm+"/followers")
time.sleep(2)
body = browser.find_element("css selector",'body')

ac = ActionChains(browser)
ac.move_to_element(body).move_by_offset(0,0).click().perform()
for i in range(40):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(1)

a = browser.find_elements("xpath", "//div[@class='x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1']")
for i in a:
	l_followers.append(i.text)

time.sleep(2)
browser.get("https://www.instagram.com/"+unm+"/following")
time.sleep(5)
body = browser.find_element("css selector",'body')
ac = ActionChains(browser)
ac.move_to_element(body).move_by_offset(0,0).click().perform()
for i in range(40):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(1)
a = browser.find_elements("xpath", "//div[@class='x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1']")
for i in a:
	l_following.append(i.text)
print("Your Followers: ", l_followers, len(l_followers))
print("Your Following: ", l_following, len(l_following))

l_extra = []
for i in l_following:
	if i not in l_followers:
		l_extra.append(i)
print("Extra:", l_extra)
