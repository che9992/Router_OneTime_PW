import requests, time
from create_pwd import CreatePasswd

class Guest_Wifi:

    def turn_on_off(self):

        if not self.status :
            print('Trying to turn on {}'.format(self.data['ssid']))
            print('Password : {}'.format(self.pw.new))
            self.new_pw()
            self.data['run'] = '1'
            self.data['action'] = 'bssidonoff'
            requests.post(self.set_url, data=self.data, headers=self.headers, cookies=self.cookies)
            print('Turned on {},ends in {} minutes \n'.format(self.data['ssid'],self.time/60))

            self.status = True

            time.sleep(self.time)

        elif self.status:
            print('Trying to turn off wifi 1')
            self.data['run'] = '0'
            self.data['action'] = 'bssidonoff'
            requests.post(self.set_url, data=self.data, headers=self.headers, cookies=self.cookies)
            print('Turned off {} \n'.format(self.data['ssid']))
            self.hard_pw()

    def new_pw(self):
        self.data['wpapsk'] = self.pw.new
        self.data['action'] = 'allsubmit'
        requests.post(self.set_url, data=self.data, headers=self.headers, cookies=self.cookies)

    def hard_pw(self):
        self.data['wpapsk'] = self.pw.hard
        self.data['action'] = 'allsubmit'
        requests.post(self.set_url, data=self.data, headers=self.headers, cookies=self.cookies)

    def __init__(self,**kwargs):
        self.headers = kwargs['Check'].headers
        self.cookies = kwargs['Login'].cookie
        self.url = kwargs['Check'].basic_url
        self.remote_port = kwargs['Check'].remote_port
        self.set_url = 'http://' + self.url + ':' + self.remote_port + '/sess-bin/timepro.cgi'

        if 'datas' not in kwargs:
            print('-----------Error--------------')
            print('You should input control datas')
            print('------------------------------')
            exit()

        else :
            self.data = kwargs['datas']

        if 'time' not in kwargs:
            self.time = 600
        else:
            self.time = kwargs['time'] * 60

        self.status = False
        self.pw = CreatePasswd()

        if 'ssid' in kwargs:
            self.data['ssid'] = kwargs['ssid']

        else:
            self.data['ssid'] = 'One Time Wifi {}'.format(kwargs['datas']['sidx'])

        if 'password' in kwargs:
            self.pw.new = kwargs['password']
