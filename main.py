#!/usr/bin/python

import requests
import time
import random
import elkacore
from threading import Thread
import sys
import signal
import argparse

ENERGY_ONCE_COUNT = 32

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--notifying', default='True')
    parser.add_argument('-c', '--credentials', default='./credentials.json')
    return parser

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
    time.sleep(5)
    while (True):
        resp = el.totalExchange('energy')
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
        time.sleep(60*60)

def careWolf():
    time.sleep(10)
    waitHours = 1
    while(True):
        resp = el.totalExchange('snow')
        resp = el.actionWolf('1')
        if (resp and (waitHours > 4 or waitHours == 1)):
            waitHours = 4
        resp = el.actionWolf('2')
        if (resp and (waitHours > 4 or waitHours == 1)):
            waitHours = 8
        resp = el.actionWolf('3')
        if (resp):
            if (resp['currentSnow'] // 1600 >= 1):
                for i in range(0, resp['currentSnow'] // 1600):
                    r = el.boostWoolf()
                    if (r):
                        r = el.actionWolf('3')
            waitHours = 8
        time.sleep(60*60*waitHours+60)

def collectBoxes():
    time.sleep(15)
    while(True):
        for i in range(1,2):
            resp = el.openBox(str(i))
            if (resp):
                if (resp['currentBox'] > 0):
                    for j in range(0, resp['currentBox']):
                        r = el.openBox(str(i))
        time.sleep(60*60*2)

if __name__ == '__main__':
    parser = createParser();
    namespace = parser.parse_args(sys.argv[1:])

    signal.signal(signal.SIGTERM, sigterm_handler)
    signal.signal(signal.SIGINT, sigint_handler)

    el = elkacore.Elochka(namespace.notifying, namespace.credentials)
    timer = 0

    chestsThread = Thread(target=collectChests)
    chestsThread.daemon = True
    chestsThread.start()

    energyThread = Thread(target=collectAndSpendEnergy)
    energyThread.daemon = True
    energyThread.start()

    careThread = Thread(target=careWolf)
    careThread.daemon = True
    careThread.start()

    boxThread = Thread(target=collectBoxes)
    boxThread.daemon = True
    boxThread.start()

    while True:
        i = 0
