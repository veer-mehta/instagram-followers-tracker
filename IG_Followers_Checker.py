import time
from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


"""
install python3:				https://www.python.org/downloads/
--> Custom installation --> Add to Path

install selenium:
pip install selenium

download chrome webdriver and save it in the same folder as the program
"""


chrome_options = webdriver.ChromeOptions()
s=service.Service('chromedriver.exe')

l_abt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
log = []
UNM = "YOUR_USERNAME"
PWD = "YOUR_PASSWORD"
RECORDS = 100							#Maximum amount among Followers and Following
SCROLL_AMT = RECORDS//12
browser = webdriver.Chrome(service = s, options = chrome_options)
browser.maximize_window()
browser.get("https://www.instagram.com")
time.sleep(2)
browser.find_element("xpath", "//input[@type = 'text']").send_keys(UNM)
browser.find_element("xpath", "//input[@type = 'password']").paswd.send_keys(PWD)
browser.find_element("xpath", "//button[@type = 'submit']").click()
time.sleep(5)

l_following, l_followers = [],[]

browser.get("https://www.instagram.com/"+UNM+"/followers")
time.sleep(2)
body = browser.find_element("css selector",'body')

ac = ActionChains(browser)
ac.move_to_element(body).move_by_offset(0,0).click().perform()
for i in range(SCROLL_AMT):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(1)

a = browser.find_elements("xpath", "//div[@class='x9f619 xjbqb8w x1rg5ohu x168nmei x103lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1']")
for i in a:
	l_followers.append(i.text)

time.sleep(2)
browser.get("https://www.instagram.com/"+UNM+"/following")
time.sleep(5)
body = browser.find_element("css selector",'body')
ac = ActionChains(browser)
ac.move_to_element(body).move_by_offset(0,0).click().perform()
for i in range(SCROLL_AMT):
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
