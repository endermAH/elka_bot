### Main configurations

#### Start session
To start session you should start playing game. Catch `init` request or any other request to `elka2020-server-vk.ereality.org`.

#### Sign
Every method has a `sign` parameter. You can get it by catching requests that appropriate methods. *Be careful, in `useEnergy()` method you should hold count of energy too.*

#### Secretory token
Get your's secretory access token [here](https://vkhost.github.io/).

#### Create credentials.json
It looks like:
```
>>> import json
>>> f = open('credentials.json', 'w')
>>> credentials = {'secretory_token': 'YOUR_TOKEN', 'sessionKey': 'YOUR_KEY'}
>>> f.write(json.dumps(credentials))
```

#### Create daemon
Modify `ExecStart` parameter in `elkabot.service` to your bot path and copy it to `/etc/systemd/system`
Than execute:
```
$ systemctl daemon-reload
$ systemctl enable elkabot.service
$ systemctl start elkabot.service
```

Now in works!
