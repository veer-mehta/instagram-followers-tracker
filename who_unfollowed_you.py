import time
from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


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
l_flw = [[],[]]
SCROLL_AMT = 100//3													#100 is max(follower, following)
browser = webdriver.Chrome(service = s, options = chrome_options)
browser.maximize_window()
browser.get("https://www.instagram.com")
time.sleep(2)
browser.find_element("xpath", "//input[@type = 'text']").send_keys(UNM)
browser.find_element("xpath", "//input[@type = 'password']").send_keys(PWD)
browser.find_element("xpath", "//button[@type = 'submit']").click()
time.sleep(5)


for x in range(2):

	time.sleep(2)
	browser.get("https://www.instagram.com/"+UNM+"/"+["followers","following"][x])
	time.sleep(5)
	body = browser.find_element("css selector",'body')

	body.click()
	time.sleep(0.5)
	for i in range(SCROLL_AMT):
		body.send_keys(Keys.PAGE_DOWN)
		time.sleep(0.5)

	a = browser.find_elements("xpath", "//span[@class='_ap3a _aaco _aacw _aacx _aad7 _aade']")
	for i in a:
		l_flw[x].append(i.text)

browser.close()

print("Your Followers: ", l_flw[0], "\nNo. of Followers: ", len(l_flw[0]))
print("Your Following: ", l_flw[1], "\nNo. of Accounts you Follow: ",  len(l_flw[1]))

l_extra = []
for i in l_flw[1]:
	if i not in l_flw[0]:
		l_extra.append(i)
print("Account which don't Follow you:", str(l_extra)[1:-1])
input()
