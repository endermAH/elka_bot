#!/usr/bin/python

import requests
import time
import random
import elkacore
from threading import Thread
import sys
import signal

def sigterm_handler(signum, frame):
    el.log('WARNING', 'Terminated by SIGTERM. Goodbye :)')
    sys.exit(0)

def sigint_handler(signum, frame):
    el.log('WARNING', 'Terminated by SIGINT. Goodbye :)')
    sys.exit(0)

def collectChests():
    while (True):
        resp = el.openChest()
        time.sleep(60*60*4+60)

signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigint_handler)

el = elkacore.Elochka()
timer = 0

message = 'Elka bot job started.'
el.notifyMe(message)

chestsThread = Thread(target=collectChests)
chestsThread.daemon = True
chestsThread.start()

while True:
    i = 0
