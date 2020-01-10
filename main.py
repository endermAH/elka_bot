#!/usr/bin/python

import requests
import time
import random
import elkacore
from threading import Thread
import sys
import signal

ENERGY_ONCE_COUNT = 45

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

#My school teacher sayd that infinit loops are evil... Am I evil?

def collectAndSpendEnergy():
    while (True):
        resp = el.factoryExchange()
        if (not resp['hasErrors']):
            collected = resp['collected']
            cur = resp['currentEnergy']
            counter = 0
            if (cur != 'unknown'):
                for i in range(1, cur // ENERGY_ONCE_COUNT):
                    lresp = el.useEnergyOnce()
                    if (lresp):
                        counter += ENERGY_ONCE_COUNT
            else:
                for i in range(1, collected // ENERGY_ONCE_COUNT):
                    lresp = el.useEnergyOnce()
                    if (lresp):
                        counter += ENERGY_ONCE_COUNT
            message = 'Ok, I spent ' + str(counter) + ' energy'
            el.log('SUCCESS', message)
            el.notifyMe(message)
        else:
            continue
        time.sleep(60*30)

signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigint_handler)

el = elkacore.Elochka()
timer = 0

message = 'Elka bot job started.'
el.notifyMe(message)

chestsThread = Thread(target=collectChests)
chestsThread.daemon = True
chestsThread.start()

energyThread = Thread(target=collectAndSpendEnergy)
energyThread.daemon = True
energyThread.start()

while True:
    i = 0
