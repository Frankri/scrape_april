#!/usr/bin/env python
from selenium import webdriver
import BeautifulSoup
import whois
import requests

'''
whois lib works correct with .com addresses only !
description: this script is allows to check websites. It pulls registration date, registrar und redirects and prints at the console. At the end it makes a screenshot
Hint! Create a 'Screenshots' folder in your working directory.
'''
# screenshots
def shots(lnk):
	browser = webdriver.Firefox()
	browser.get(lnk)
	safe_lnk = lnk.replace('/', '_')
	browser.save_screenshot('Screenshots/scr-pic-' + safe_lnk + '.png')
	browser.quit()
	
# whois check (added 4/14/2014)
def whois_chck(lnk):
	w = whois.whois(lnk)
	reg_date = w.creation_date
	registrar = w.registrar
	return (reg_date, registrar)
	
# content check (added 4/15/2014)
def content(lnk):
	r = requests.get(lnk, allow_redirects=True)
	cont = r.text.encode("utf-8")
	hist = r.history
	if 301 in r.history:
		print r.url
	else:
		pass
	red = r.url
	return red


# manually type in and extension if needful
name = raw_input("URL:")
if 'http://' in name or 'https://' in name:
    lnk = name
else:
    lnk = 'http://' + name

# output URL, date of registration, registrar
(reg_date, registrar) = whois_chck(lnk)

# output requests
red = content(lnk)

print lnk, 'registered at: ', reg_date, registrar, 'redirected to:', red

#shots(lnk)
