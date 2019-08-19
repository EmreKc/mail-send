import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
import pandas as pd

x = os.popen('echo %cd%').read()
_path = str(x)[:len(str(x))-1] + "\\mails.xlsx"

df = pd.read_excel(_path)

mails = df['mails']
email = df['email'][0]
print(email)
ps = df['password'][0]
print(ps)
sbj = df['subject'][0]
print(sbj)
bdy = df['body'][0]
print(bdy)

options = Options()
options.headless = True
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary, options=options)
driver.get("https://webmail1.hostinger.web.tr/")
user = driver.find_element_by_id("rcmloginuser")
user.send_keys(email) # mail adresini yaz
pss = driver.find_element_by_id("rcmloginpwd")
pss.send_keys(ps) #şifreni yaz
btn = driver.find_element_by_id("rcmloginsubmit")
btn.click()
time.sleep(1)
#count = 0
if "Gelen" in driver.title:
	for mail in mails:
		#print(mail)
		time.sleep(1)
		driver.implicitly_wait(10)
		ilet = driver.find_element_by_id("rcmbtn108")
		ilet.click()
		time.sleep(1)
		driver.implicitly_wait(5)
		to = driver.find_element_by_id("_to")
		to.send_keys(mail)
		subject = driver.find_element_by_id("compose-subject")
		subject.send_keys(sbj)
		body = driver.find_element_by_id("composebody")
		body.send_keys(bdy)
		send = driver.find_element_by_id("rcmbtn107")
		send.click()
		#count +=1
		#print(count)

		while 'İleti Gönder' != driver.find_element_by_id("rcmbtn108").text:
			#print(0)
			time.sleep(0.5)
driver.quit()
print("ok")
