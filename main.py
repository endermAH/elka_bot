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
    el.log('TEST', resp)
    if (resp['award'] == 'no award' or resp['award'] == 'no data'):
        message = 'I\'ve tried to open the chest, but there is no award :('
        el.log('WARNING', message)
    else:
        massage = 'I\'ve opened the chest: \n\r Snow:' + str(resp['award']['resource']['money1']) + '\n\r Energy: ' + str(resp['award']['resource']['energy']) + '\n\r Diamonds: ' + str(resp['award']['resource']['cash']) + '\n\r Keys: ' + str(resp['award']['resource']['keys'])
        el.log('SUCCESS', message)
    el.notifyMe(message)

    resp = el.factoryExchange()
    message = 'I collected ' + str(resp['collected']) + ' energy.\n\r Now there is ' + str(resp['currentEnergy']) + ' energy'
    el.log('SUCCESS', message)
    el.notifyMe(message)

    time.sleep(60*60*4+60)
