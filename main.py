#!/usr/bin/python

import requests
import time
import random
import elkacore

el = elkacore.Elochka()
timer = 0

message = 'Elka bot job started.'
el.notifyMe(message)

while (True):
    resp = el.openChest()
    resp = el.factoryExchange()

    time.sleep(60*60*4+60)
