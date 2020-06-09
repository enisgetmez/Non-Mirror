from selenium import webdriver
import time


def getfollowing(username):
	browser = webdriver.Firefox()
	browser.get("https://gramho.com/following/" + username)
	time.sleep(3)
	for scroll in range(0,15):
		browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(0.3)
	userlist = open("userlist.txt", "w")

	kullanicilar = browser.find_elements_by_css_selector("span[class$='username']")
	for kullanici in kullanicilar:
		userlist.write(kullanici.text.replace("@", "") + "\n")
		print(kullanici.text.replace("@", ""))