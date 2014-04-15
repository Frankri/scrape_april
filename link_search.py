import requests
from selenium import webdriver

def shots(lnk):
	browser = webdriver.Firefox()
	browser.get(lnk)
	safe_lnk = lnk.replace('/', '_')
	browser.save_screenshot('screenshots/scr-pic-' + safe_lnk + '.png')
	browser.quit()

# manuelle Eingabe des Links
name = raw_input("URL:")
if 'http://' in name or 'https://' in name:
    lnk = name
else:
    lnk = 'http://' + name
print lnk

shots(lnk)


r = requests.get(lnk)
content = r.text.encode("utf-8")

l = len(content)
link_counter = 0

pos1b = 0
for e in range(0,l-1):
    link_list = []
    pos1 = content.find('href="',pos1b)
    pos1a = pos1+6
    pos1b = content.find('"',pos1a)
    link = content[pos1a:pos1b]
    link_counter += 1
    print link_counter, link
    link_list = link_list.append(link)
 
link_text = open('results.txt', 'r+')   
link_text.write(str(link_list))



