#!/usr/bin/python
import pynotify

class Displayer(object):
    def __init__(self):
        """
        Class that displays the notification
        
        """
        if not pynotify.init("icon-summary-body"):
            sys.exit(1)
        self.notifier = pynotify.Notification


    def display(self,msg):
        self.notifier(msg).show()


if __name__ == '__main__':
    d = Displayer()
  
    d.display("Hi There")
