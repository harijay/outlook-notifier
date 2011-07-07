#!/usr/bin/python
import spynner
from spynner import browser
import pyquery
import pynotify


agent = browser.Browser()
# agent.create_webview(True)
# agent.show()
agent.load("https://webmail.constellationpharma.com")
agent.fill("input[name=username]","hari.jayaram")
agent.fill("input[name=password]","Eer101cer101")
agent.click("input[type=submit]")
agent.wait_load()
d = pyquery.PyQuery(agent.html)
p = pynotify.Notification("New email title: " + str(d(".frst a"))).show()



