from pyvirtualdisplay import Display
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib2

display = Display(visible=0, size=(800,600))
display.start()
name=raw_input("song name [Ex.Love me Like you do.mp3]")
driver = webdriver.Chrome('/home/mpmaurya/Documents/Project/SCDownloader/chromedriver')
driver.get("http://scdownloader.net")
url=driver.find_element_by_id("songURL")
url.send_keys(sys.argv[1])
driver.find_element_by_tag_name("button").click()
driver.implicitly_wait(5)
down=driver.find_element_by_link_text("Download Link")
dlink=down.get_attribute("href")
print ("Downloading Song ",sys.argv[1])
f=urllib2.urlopen(dlink)
song=f.read()
with open(name,"wb") as bits:
    bits.write(song)


