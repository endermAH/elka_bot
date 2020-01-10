#!/usr/bin/python

import requests
import time
import random

class Elochka:
    sessionKey = 'ac145905ef88688480751b733397774b3551877b'
    version = '19'

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

    def __parceOpEnergy(self, op):
        for i in range(0,4):
            if (str(i) in op):
                if (op[str(i)]['path'] == '/resource/energy'):
                    return op[str(i)]['value']
        return 'unknown'

    def __causeError(self, error, data):
        print('Elka ERROR caused: ' + error + '\nData: ')
        print(data)

    def notifyMe(self, msg):
        random_id = random.randrange(0,100000,1)
        url = 'https://api.vk.com/method/messages.send?peer_id=225299625&random_id=' + str(random_id) + '&message=' + msg + '&access_token=85681fa2463297bc96226c3e4070e4eecf0654fdd088ec266697505cde91b86b8ef0c33303caf5ced2ae7&v=5.103'
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
        sign = '7437ad085d5eb02b131c52be815648cd'
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
            currentEnergy = self.__parceOpEnergy(r['op'])
        else:
            self.__causeError('No "op" field in responce', r)
            currentEnergy = 'unknown'

        data = {
            'collected': collected,
            'currentEnergy': currentEnergy,
            'hasErrors': (error != 'False')
        }
        return data

    def totalExchange(self, resource):
        referer = {
            'energy': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=2&sid=3ac422480242450d97a53ed87f644b870e02591b2eeb51d11d318a4fa1e8f8f27a346756b773f45170e76&secret=ceaf4d1309&access_token=afec406c2f63b75313021a08cdbfcdc8391719f47254fe98f99fc391f944f260c0636aba643602b41a871&user_id=225299625&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_4d9f4d4083fdfa1e36&referrer=unknown&lc_name=71eb096e&platform=web&hash=',
            'ruby': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=2&sid=3ac422480242450d97a53ed87f644b870e02591b2eeb51d11d318a4fa1e8f8f27a346756b773f45170e76&secret=ceaf4d1309&access_token=afec406c2f63b75313021a08cdbfcdc8391719f47254fe98f99fc391f944f260c0636aba643602b41a871&user_id=225299625&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_4d9f4d4083fdfa1e36&referrer=unknown&lc_name=71eb096e&platform=web&hash=',
            'snow': '',
            'coin': ''
        }
        sign = {
            'energy': '408d8b5d6d3bde46ec6e46bd0f73d4f4',
            'ruby': 'a0850c410bbfa9d99246e03646eecf7d',
            'snow': '',
            'coin': ''
        }
        contentLength = {
            'energy': '261',
            'ruby': '',
            'snow': '',
            'coin': ''
        }
        name = {
            'energy': 'winterFactory',
            'ruby': 'designObject1',

        }
        url = 'https://elka2020-server-vk.ereality.org/generator/exchange'
        headers = self.mainHeaders
        headers.update({
            'Referer': referer[resource],
            'Content-Length': contentLength[resource],
            })
        data = '{"params":{"name":"' + name[resource] + '"},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":18,"clientPlatform":"js","sign":"' + sign[resource] + '"}'
        r = requests.post(url, data=data, headers=headers)
        r = r.json()
        print(r)
        data = {
            'get': r['data']['award']['resource']['energy'],
        }
        return data

    def useEnergyOnce(self):
        count = 20
        sign = '6668935bc568b6944fa998e2e90516fa'
        url = 'https://elka2020-server-vk.ereality.org/object/useEnergy'
        headers = self.mainHeaders
        headers.update({
            'Content-Length': '289',
            'Referer': 'https://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=2&sid=c2025445a0ea4177c651f75667fff7faa940972eb9cc945ac89a6b0a6d2ab4d7eb2ad22b57c892365c6a7&secret=6888e61788&access_token=d82aa377a093f25422e4057f99108704c7ff532c9db51304fb1e15a4b2143dea6710275362c26d466e23c&user_id=225299625&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_4d9f4d4083fdfa1e36&referrer=unknown&lc_name=8daf2b67&platform=web&hash=',
        })

        data = '{"params":{"objectName":"winterMaiden","count":' + str(count) + ',"window":1},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":18,"clientPlatform":"js","sign":"' + sign + '"}'
        # print(data)
        r = requests.post(url, data=data, headers=headers)
        r = r.json()
        print(r)
        data = {
            'get': r,
        }
        return data

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
        sign = '477b818da66f35015b8356520ee12d02'
        url = 'https://elka2020-server-vk.ereality.org/chest/open'
        headers = self.mainHeaders
        headers.update({
            'Content-Length': '250',
            'Referer': 'ttps://elka2020-client-vk.ereality.org/?api_url=https://api.vk.com/api.php&api_id=7113532&api_settings=2368775&viewer_id=225299625&viewer_type=0&sid=dc3c436e35e89ce086568cdfab418cde7400f4c45f09255f5ea4a3a29c6d465b94ddb8f28774d93eeea5d&secret=55a81b0b30&access_token=51a0f41f89a45ed21be37d6ab0ea9c00d20f66710faedb54b33614df78d05ad632f1594f6bc47a02e20be&user_id=0&group_id=0&is_app_user=1&auth_key=a8d561b58babc3b79218936fa82a0684&language=0&parent_language=0&is_secure=1&stats_hash=1dfee73734f66879bf&ads_app_id=7113532_8abd913ee8afe00b53&referrer=unknown&lc_name=6ddc78f3&platform=web&hash='
        })
        data = '{"params":{"chestId":2},"uid":125744,"suid":"225299625","aid":"7113532","authKey":"de7afe2878276a4091b89bd70ee1d9d1","sessionKey":"' + self.sessionKey + '","version":' + self.version + ',"clientPlatform":"js","sign":"' +  sign + '"}'
        r = requests.post(url, data=data, headers=headers)
        r = r.json()

        if ('data' in r):
            if ('award' in r['data']):
                 award = r['data']['award']
            else:
                award = 'no award'
        else:
            award = 'no data'
            self.__causeError(award, r)

        data = {
            'award': award,
            'r': r
        }
        return data


el = Elochka()
timer = 0

message = 'Elka bot job started.'
el.notifyMe(message)

while (True):
    resp = el.openChest()
    print(resp['r'])
    if (resp['award'] == 'no award' or resp['award'] == 'no data'):
        message = 'I\'ve tried to open the chest, but there is no award :('
    else:
        massage = 'I\'ve opened the chest: \n\r Snow:' + str(resp['award']['resource']['money1']) + '\n\r Energy: ' + str(resp['award']['resource']['energy']) + '\n\r Diamonds: ' + str(resp['award']['resource']['cash']) + '\n\r Keys: ' + str(resp['award']['resource']['keys'])
    el.notifyMe(message)

    resp = el.factoryExchange()
    message = 'I collected ' + str(resp['collected']) + ' energy.\n\r Now there is ' + str(resp['currentEnergy']) + ' energy'
    print(message)
    el.notifyMe(message)

    time.sleep(60*60*4+60)


# responce.json()
print(responce)

# el.getSessionKey()
#print(el.sessionKey)
#resp = el.factoryExchange()
#print('Got energy: ' + str(resp['collected']) + '\nCurrent energy: ' + str(resp['currentEnergy']))
# resp = el.useEnergy(0)
# print(resp['used'])
# resp = el.openChest();
# print(resp['award'])
# resp = el.totalExchange('energy')
# print(resp['get'])
