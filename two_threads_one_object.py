import time
import json
import random
import threading

class FrequentChanges(object):
    """ This object will have changes made to it frequently
    by the Changer thread"""
    def __init__(self):
        self.name = "Hello"
        self.changes = ''

class Changer(threading.Thread):
    """ This thread will be making changes to the FrequentChanges object"""
    def __init__(self, fc ):
        threading.Thread.__init__(self)
        self.fc = fc
        self.stop = None

    def run(self):
        print("Starting Changer...")
        while not self.stop:
            if random.randint(0,1) == 1:
                self.fc.changes = time.time()
        print("Changer stopped...")


class Saver(threading.Thread):
    """ This thread will periodically save updates to the fc object"""
    def __init__(self, fc):
        threading.Thread.__init__(self)
        self.fc = fc
        self.stop = None

    def run(self):
        print("Starting Saver...")
        while not self.stop:
            with open('frequentchanges.txt', 'w') as fp:
                print(json.dumps(self.fc.__dict__), file = fp, end = "")
        print("Saver stopped...")


fc = FrequentChanges()
c = Changer(fc)
s = Saver(fc)

c.start()
s.start()

input("Running (press enter to stop)...")
print('Shutting down...')
c.stop = 1
s.stop = 1
