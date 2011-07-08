#!/usr/bin/python
import spynner
from spynner import browser
import pyquery
import pynotify
import time
import private

agent = browser.Browser()
# agent.create_webview(True)
# agent.show()
agent.load("https://webmail.constellationpharma.com")
agent.fill("input[name=username]",private.uname)
agent.fill("input[name=password]",private.password)
agent.click("input[type=submit]")
agent.create_webview(True)

for i in range(10):
    time.sleep(300)
#    agent.show()
    agent.click("a[title=Check Messages]")
    agent.wait_load()
    d = pyquery.PyQuery(agent.html)
    time.sleep(5)
    p = pynotify.Notification("New email title: " + str(d(".frst a"))).show()


