import requests
import time
import random
import json

class Elochka:
    sessionKey = ''
    version = '19'
    logfile = 'LOG FILE'
    secretoryToken = ''
    myId = '225299625'
    logPath = ''
    enableNotifying = 'True'

    mainHeaders = {
        'Host': 'elka2020-server-vk.ereality.org',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'https://elka2020-client-vk.ereality.org',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    def __init__(self, enableNotifying, credentialsPath):
        credentialsFile = open(credentialsPath)
        credentials = json.loads(credentialsFile.read())
        self.sessionKey = credentials['sessionKey']
        self.secretoryToken = credentials['secretory_token']
        self.logPath = credentials['logPath']
        self.enableNotifying = enableNotifying
        message = 'Elka bot job started.'
        self.notifyMe(message)

    def __parceOpResource(self, op, res):
        for i in op:
            if (str(i) in op):
                if (op[str(i)]['path'] == '/resource/' + res):
                    return op[str(i)]['value']
        return 'unknown'

    def __causeError(self, error, data):
        self.log('ERROR', error + '\nResponce: ' + str(data))

    def stageUpObject(self, object):
        sign = {
            'winterMaiden': '500f02ba1b759f3bd4764e83050bc401'
        }

        url = 'https://elka2020-server-vk.ereality.org/object/stageUp'
        headers = self.mainHeaders
        headers.update({
            'Content-Length': '266',
            'Referer': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=6b242ea2cb97bb00f6044a70ca21757a1e772092bc08d2c4bfb39905464e09015ce92031a3d9b793de9cc&secret=dd30cb295a&access_token=4c5db7a80c4f27b495d398fa081935ac77092992c9078570d71b097149abca31232441e27d12f89d148f7&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_11c2bc5d4b01bb73ee&referrer=unknown&lc_name=dade34fa&platform=web&hash='
        })

        data = '{"params":{"objectName":"' + object + '"},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":' + self.version + ',"clientPlatform":"js","sign":"' + sign[object] + '"}'

        r = requests.post(url, data=data, headers=headers)
        r = r.json()

        error = ''

        if ('error' in r):
            self.__causeError(r['error']['text'], r)
            return r['error']['text']

        if ('data' in r):
            if ('award' in r['data']):
                if ('resource' in r['data']['award']):
                    if ('money1' in r['data']['award']['resource']):
                        collected = r['data']['award']['resource']['money1'] #Hardcoded award attention!
                    else:
                        error += 'Snow error'
                else:
                     error += 'Resource error'
            else:
                 error += 'Award error'
        else:
            error += 'Data error'

        if (error != ''):
            self.__causeError(error, r)

        resp = {
            'collected': collected
        }

        self.log('TEST', r)

        if ((not ('error' in r)) and (error == '')):
            message = 'Object ' + object + ' staged up'
            self.log('SUCCESS', message)
            self.notifyMe(message)

    def log(self, type, msg):

        LOG_TYPE = {
            'TEST': '\033[36mTEST:\033[0m',
            'SUCCESS': '\033[32mSUCCESS:\033[0m',
            'ERROR': '\033[31mERROR:\033[0m',
            'WARNING': '\033[35mWARNING:\033[0m',
        }
        self.logfile = open(self.logPath, 'a')
        self.logfile.write(LOG_TYPE[type] + ' ' + str(msg) + '\n\r')
        self.logfile.close()
        print(LOG_TYPE[type] + ' ' + str(msg))

    def notifyMe(self, msg):
        if (self.enableNotifying == 'True'):
            random_id = random.randrange(0,100000,1)
            url = 'https://api.vk.com/method/messages.send?peer_id=' + self.myId + '&random_id=' + str(random_id) + '&message=' + msg + '&access_token=' + self.secretoryToken + '&v=5.103'
            responce = requests.get(url)
            print(responce.content)

    def getSessionKey(self):
        url = 'https://elka2020-server-vk.ereality.org/canvas/show?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=9090c6a092e51714593c9550cb7e74edbead0f63d9334546224f80914079665b680307feddd0d99374e2f&secret=932fa69ab4&access_token=828ebf001e29d563422c4f94e4d3a5269fa01f59cdf30f2b7b2669983dbe4fbd3806f7fcf61bbad9425ae&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_4d9f4d4083fdfa1e36&referrer=unknown&lc_name=92c0bd26&platform=web&hash='
        headers = {
            'Host': 'elka2020-server-vk.ereality.org',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'Origin': 'https://elka2020-client-vk.ereality.org',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=9090c6a092e51714593c9550cb7e74edbead0f63d9334546224f80914079665b680307feddd0d99374e2f&secret=932fa69ab4&access_token=828ebf001e29d563422c4f94e4d3a5269fa01f59cdf30f2b7b2669983dbe4fbd3806f7fcf61bbad9425ae&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_4d9f4d4083fdfa1e36&referrer=unknown&lc_name=92c0bd26&platform=web&hash=',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        data = 'api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=9090c6a092e51714593c9550cb7e74edbead0f63d9334546224f80914079665b680307feddd0d99374e2f&secret=932fa69ab4&access_token=828ebf001e29d563422c4f94e4d3a5269fa01f59cdf30f2b7b2669983dbe4fbd3806f7fcf61bbad9425ae&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_4d9f4d4083fdfa1e36&referrer=unknown&lc_name=92c0bd26&platform=web&hash='
        r = requests.post(url, data=data, headers=headers)
        r = r.json()
        self.sessionKey = r['sessionKey']

    def factoryExchange(self):
        sign = '42e808ab34ded6d5351245f8c21fca38'
        url = 'https://elka2020-server-vk.ereality.org/generator/exchange'
        headers = self.mainHeaders
        headers.update({
            'Referer': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=2&sid=ab6c4b0ca1201e797c581639e54e624f7856c74003f447349118c2326a2433d3c457a7781640f45d91b81&secret=888d07bcd0&access_token=dfdb017cecfd3859b436161bdaaeacea2ede6fac6718ec86f2830e456a2fb10fbfff235dc9057927f67af&user_id=225299625&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_4d9f4d4083fdfa1e36&referrer=unknown&lc_name=2a2bf5cc&platform=web&hash=',
            'Content-Length': '253',
            })

        data = '{"params":{"name":"farm1"},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":' + self.version + ',"clientPlatform":"js","sign":"' + sign + '"}'
        # print(data)
        r = requests.post(url, data=data, headers=headers)
        r = r.json()

        error = ''
        collected = '0'

        if ('error' in r):
            self.__causeError(r['error']['text'], r)
            return r['error']['text']

        if ('data' in r):
            if ('award' in r['data']):
                if ('resource' in r['data']['award']):
                    if ('energy' in r['data']['award']['resource']):
                        collected = r['data']['award']['resource']['energy']
                    else:
                        error += 'energy error'
                else:
                     error += 'resource error'
            else:
                 error += 'award error'
        else:
            error += 'data error'

        if (error != ''):
            self.__causeError(error, r)

        if ('op' in r):
            currentEnergy = self.__parceOpResource(r['op'], 'energy')
        else:
            self.__causeError('No "op" field in responce', r)
            currentEnergy = 'unknown'

        resp = {
            'collected': collected,
            'currentEnergy': currentEnergy,
            'hasErrors': (error != '')
        }

        message = 'I collected ' + str(resp['collected']) + ' energy.\n\rNow there is ' + str(resp['currentEnergy']) + ' energy'
        self.log('SUCCESS', message)
        self.notifyMe(message)

        return resp

    def totalExchange(self, resource):
        sign = {
            'energy': 'cab6fb1786c2dbca452be2caa52463f5',
            'ruby': 'a0850c410bbfa9d99246e03646eecf7d', # not True!!!
            'snow': '32f7730d2a485944f89aa3fb5f394043',
            'coin': ''
        }
        contentLength = {
            'energy': '261',
            'ruby': '',
            'snow': '260',
            'coin': ''
        }
        name = {
            'energy': 'winterFactory',
            'ruby': 'designObject1',
            'snow': 'winterMaiden'
        }
        trueNames = {
            'energy': 'energy',
            'ruby': 'cash',
            'snow': 'money1',
            'coin': 'coins'
        }
        referer = {
            'energy': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=7b30cec28e120c3d05539e88b40767794209576d1c1414b627e29f8cbcbfbd9a7bc61aef81420d4d7886d&secret=102dbcee88&access_token=057bd34cf38ff6e67bc06ee903cda2f4195878cdf04b287006ab9a9dbd583723492624df00f5c6d38f1f4&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_6108e538eacd7a56e9&referrer=unknown&lc_name=6f6e3ed2&platform=web&hash=',
            'ruby': '',
            'snow': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=7b30cec28e120c3d05539e88b40767794209576d1c1414b627e29f8cbcbfbd9a7bc61aef81420d4d7886d&secret=102dbcee88&access_token=057bd34cf38ff6e67bc06ee903cda2f4195878cdf04b287006ab9a9dbd583723492624df00f5c6d38f1f4&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_6108e538eacd7a56e9&referrer=unknown&lc_name=6f6e3ed2&platform=web&hash=',
            'coin': ''
        }
        url = 'https://elka2020-server-vk.ereality.org/generator/exchange'
        headers = self.mainHeaders
        headers.update({
            'Referer': referer[resource],
            'Content-Length': contentLength[resource],
            })
        data = '{"params":{"name":"' + name[resource] + '"},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":' + self.version + ',"clientPlatform":"js","sign":"' + sign[resource] + '"}'

        r = requests.post(url, data=data, headers=headers)
        r = r.json()

        if ('error' in r):
            self.__causeError(r['error']['text'], r)
            return False

        error = ''

        if ('data' in r):
            if ('award' in r['data']):
                if ('resource' in r['data']['award']):
                    if ('energy' in r['data']['award']['resource']):
                        collected = r['data']['award']['resource'][trueNames[resource]]
                    else:
                        error += 'little error'
                else:
                     error += 'resource error'
            else:
                 error += 'award error'
        else:
            error += 'data error'

        if (error != ''):
            self.__causeError(error, r)
            return False

        resp = {
            'get': collected,
            'r': r
        }

        message = 'I collected ' + str(collected) + ' ' + resource
        self.log('SUCCESS', message)
        self.notifyMe(message)

        return resp

    def useEnergyOnce(self):
        count = 32
        sign = 'd0d5479233f9a3842669beeae2b57a05'
        url = 'https://elka2020-server-vk.ereality.org/object/useEnergy'
        headers = self.mainHeaders
        headers.update({
            'Content-Length': '289',
            'Referer': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=2&sid=c2025445a0ea4177c651f75667fff7faa940972eb9cc945ac89a6b0a6d2ab4d7eb2ad22b57c892365c6a7&secret=6888e61788&access_token=d82aa377a093f25422e4057f99108704c7ff532c9db51304fb1e15a4b2143dea6710275362c26d466e23c&user_id=225299625&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_4d9f4d4083fdfa1e36&referrer=unknown&lc_name=8daf2b67&platform=web&hash=',
        })

        data = '{"params":{"objectName":"winterMaiden","count":' + str(count) + ',"window":1},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":' + self.version + ',"clientPlatform":"js","sign":"' + sign + '"}'

        r = requests.post(url, data=data, headers=headers)
        r = r.json()

        if ('error' in r):
            self.__causeError(r['error']['text'], r)
            if (r['error']['text'] == 'object wait a new level'):
                self.stageUpObject('winterMaiden')
            return False

        if ('op' in r):
            currentEnergy = self.__parceOpResource(r['op'], 'energy')
        else:
            self.__causeError('No "op" field in responce', r)
            currentEnergy = 'unknown'

        resp = {
            'r': r,
            'currentEnergy': currentEnergy,
        }

        self.log('SUCCESS', 'Spent ' + str(count) + ' energy. Current energy: ' + str(currentEnergy))
        return resp

    def useEnergy(self, count):
        used = 0
        for i in range(1, count):
            self.useEnergyOnce()
            used += 20
        data = {
            "used": used
        }
        return data

    def openChest(self):
        sign = '0727c0000d89f2ab121584ba45f258ae'
        url = 'https://elka2020-server-vk.ereality.org/chest/open'
        headers = self.mainHeaders
        headers.update({
            'Content-Length': '250',
            'Referer': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=dc3c436e35e89ce086568cdfab418cde7400f4c45f09255f5ea4a3a29c6d465b94ddb8f28774d93eeea5d&secret=55a81b0b30&access_token=51a0f41f89a45ed21be37d6ab0ea9c00d20f66710faedb54b33614df78d05ad632f1594f6bc47a02e20be&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_8abd913ee8afe00b53&referrer=unknown&lc_name=6ddc78f3&platform=web&hash='
        })
        data = '{"params":{"chestId":2},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":' + self.version + ',"clientPlatform":"js","sign":"' +  sign + '"}'
        r = requests.post(url, data=data, headers=headers)
        r = r.json()

        if ('error' in r):
            self.__causeError(r['error']['text'], r)
            if (r['error']['text'] == 'object wait a new level'):
                self.stageUpObject('winterMaiden')
            return r['error']['text']

        if ('data' in r):
            if ('award' in r['data']):
                 award = r['data']['award']
            else:
                award = 'No award in open chest responce!'
        else:
            award = 'No data in open chest responce!'
            self.__causeError(award, r)

        resp = {
            'award': award,
            'r': r
        }

        self.log('TEST', resp)
        if (resp['award'] == 'No award in open chest responce!' or resp['award'] == 'No data in open chest responce!'):
            message = 'I\'ve tried to open the chest, but there is no award :('
            self.log('WARNING', message)
        else:
            message = 'I\'ve opened the chest: \n\r Snow:' + str(resp['award']['resource']['money1']) + '\n\r Energy: ' + str(resp['award']['resource']['energy']) + '\n\r Diamonds: ' + str(resp['award']['resource']['cash']) + '\n\r Keys: ' + str(resp['award']['resource']['keys'])
            self.log('SUCCESS', message)
        self.notifyMe(message)

        return resp

    def stageUpWolf(self):
        sign = 'eee6b67a41cd51f616e75daf6c81b3e3'
        url = 'https://elka2020-server-vk.ereality.org/animal/stageUp'
        headers = self.mainHeaders
        headers.update({
            'Content-Length': '251',
            'Referer': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=6b242ea2cb97bb00f6044a70ca21757a1e772092bc08d2c4bfb39905464e09015ce92031a3d9b793de9cc&secret=dd30cb295a&access_token=4c5db7a80c4f27b495d398fa081935ac77092992c9078570d71b097149abca31232441e27d12f89d148f7&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_11c2bc5d4b01bb73ee&referrer=unknown&lc_name=dade34fa&platform=web&hash='
        })

        data = '{"params":{"animalId":1},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":' + self.version + ',"clientPlatform":"js","sign":"' + sign + '"}'

        if ('error' in r):
            self.__causeError(r['error']['text'], r)
            return False

        resp = {
            'r': r
        }

        message = 'Your wolf staged up!'
        self.log('SUCCESS', message)
        self.notifyMe(message)

    def actionWolf(self, actionId):
        sign = {
            '1': '5418409abf16fbc98d47ffe65f8d1901', #feed
            '2': 'e367b74ffe33c3d9d14667f5de2e5450', #sleep
            '3': 'b4fb93fc2ee0087fd202b084b485c98d', #play
        }

        actionName = {
        '1': 'feed',
        '2': 'sleep',
        '3': 'play',
        }

        url = 'https://elka2020-server-vk.ereality.org/animal/start'
        headers = self.mainHeaders
        headers.update({
            'Content-Length': '264',
            'Referer': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=6b242ea2cb97bb00f6044a70ca21757a1e772092bc08d2c4bfb39905464e09015ce92031a3d9b793de9cc&secret=dd30cb295a&access_token=4c5db7a80c4f27b495d398fa081935ac77092992c9078570d71b097149abca31232441e27d12f89d148f7&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_11c2bc5d4b01bb73ee&referrer=unknown&lc_name=dade34fa&platform=web&hash='
        })

        data = '{"params":{"animalId":1,"actionId":' + actionId + '},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":' + self.version + ',"clientPlatform":"js","sign":"' + sign[actionId] + '"}'

        r = requests.post(url, data=data, headers=headers)
        r = r.json()

        if ('error' in r):
            self.__causeError(r['error']['text'], r)
            if (r['error']['text'] == 'object wait a new level'):
                self.stageUpWolf()
            self.notifyMe('I tried to ' + actionName[actionId] + ' your wolf, but this ' + r['error']['text'])
            return False

        if ('op' in r):
            currentSnow = self.__parceOpResource(r['op'], 'money1')
        else:
            self.__causeError('No "op" field in responce', r)
            currentSnow = 'unknown'

        resp = {
            'r': r,
            'currentSnow': currentSnow
        }

        message = 'I had ' + actionName[actionId] + 'ed your wolf'
        self.log('SUCCESS', message)
        self.notifyMe(message)

        return resp

    def openBox(self, boxId):
        sign = {
            '1': 'e6753e25c1f78b86eb93194219cc5b90',
            '2': 'fc8834b12d4903e50485ec60b64d8285',
            '3': '',
        }

        boxName = {
        '1': 'little',
        '2': 'middle',
        '3': 'gold',
        }

        url = 'https://elka2020-server-vk.ereality.org/box/open'
        headers = self.mainHeaders
        headers.update({
            'Content-Length': '250',
            'Referer': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=6b242ea2cb97bb00f6044a70ca21757a1e772092bc08d2c4bfb39905464e09015ce92031a3d9b793de9cc&secret=dd30cb295a&access_token=4c5db7a80c4f27b495d398fa081935ac77092992c9078570d71b097149abca31232441e27d12f89d148f7&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_11c2bc5d4b01bb73ee&referrer=unknown&lc_name=dade34fa&platform=web&hash='
        })

        data = '{"params":{"boxId":"' + boxId + '"},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":' + self.version + ',"clientPlatform":"js","sign":"' + sign[boxId] + '"}'

        r = requests.post(url, data=data, headers=headers)
        r = r.json()

        if ('error' in r):
            self.__causeError(r['error']['text'], r)
            self.notifyMe('I tried to open ' + boxName[boxId] + ' , but - ' + r['error']['text'])
            return False

        if ('op' in r):
            currentBox = self.__parceOpResource(r['op'], 'box1')
        else:
            self.__causeError('No "op" field in responce', r)
            currentBox = 'unknown'

        message = 'I opened ' + boxName[boxId] + ' and got this award:\n\r'
        if ('data' in r):
            for i in r['data']:
                for j in r['data'][i]['resource']:
                    message += j + ': ' +  str(r['data'][i]['resource'][j]) + '\n\r'
        else:
            message = 'Data loss sorry :('
            return False

        self.log('SUCCESS', message)
        self.notifyMe(message)

        resp = {
            'currentBox': currentBox,
            'r': r
        }

        return resp

    def boostWoolf(self):
        sign = '630ab24560d291205e4e8ebf54322438'
        url = 'https://elka2020-server-vk.ereality.org/animal/boost'
        headers = self.mainHeaders
        headers.update({
            'Content-Length': '264',
            'Referer': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=7b30cec28e120c3d05539e88b40767794209576d1c1414b627e29f8cbcbfbd9a7bc61aef81420d4d7886d&secret=102dbcee88&access_token=057bd34cf38ff6e67bc06ee903cda2f4195878cdf04b287006ab9a9dbd583723492624df00f5c6d38f1f4&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_6108e538eacd7a56e9&referrer=unknown&lc_name=6f6e3ed2&platform=web&hash='
        })

        data = '{"params":{"animalId":1,"actionId":3},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":' + self.version + ',"clientPlatform":"js","sign":"' + sign + '"}'

        r = requests.post(url, data=data, headers=headers)
        r = r.json()

        if ('error' in r):
            self.__causeError(r['error']['text'], r)
            self.notifyMe('I tried to boost sleeping your wolf, but this ' + r['error']['text'])
            return False

        if ('op' in r):
            currentSnow = self.__parceOpResource(r['op'], 'money1')
        else:
            self.__causeError('No "op" field in responce', r)
            currentSnow = 'unknown'

        resp = {
            'r': r,
            'currentSnow': currentSnow
        }

        message = 'I had boosted sleeping your wolf'
        self.log('SUCCESS', message)
        self.notifyMe(message)

        return resp
