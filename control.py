import requests, time
from create_pwd import CreatePasswd

class Guest_Wifi:

    def turn_on(self):
        print('Trying to turn on wifi 1')
        on = requests.post(self.set_url, data=self.on_data, headers=self.headers, cookies=self.cookies)
        print('Turned on guest wifi 1,ends in {} minutes \n'.format(self.time/60))
        on.close()

    def turn_off(self):
        print('Trying to turn off wifi 1')
        off = requests.post(self.set_url, data=self.off_data, headers=self.headers, cookies=self.cookies)
        print('Turned off guest wifi 1\n')
        off.close()

    def new_pw(self):
        print('New Password : {}'.format(self.pw.new))
        print('Trying to change password as new password')
        new = requests.post(self.set_url, data=self.pw_head_data+self.pw.new+self.pw_tail_data, headers=self.headers, cookies=self.cookies)
        print('guest wifi 1 changed password as new password\n')
        new.close()

    def hard_pw(self):
        print('Hard Password : {}'.format(self.pw.hard))
        hard = requests.post(self.set_url, data=self.pw_head_data+self.pw.hard+self.pw_tail_data, headers=self.headers, cookies=self.cookies)
        print('guest wifi 1 changed password as hard password')
        hard.close()

    def __init__(self,**kwargs):
        self.time = kwargs['time'] * 60
        self.headers = kwargs['Check'].headers
        self.cookies = kwargs['Login'].cookie
        self.url = kwargs['Check'].basic_url
        self.remote_port = kwargs['Check'].remote_port
        self.set_url = 'http://' + self.url + ':' + self.remote_port + '/sess-bin/timepro.cgi'
        self.on_data = kwargs['datas'][0]
        self.off_data = kwargs['datas'][1]
        self.pw_head_data = kwargs['datas'][2]
        self.pw_tail_data = kwargs['datas'][3]
        self.pw = CreatePasswd()

        self.turn_on()
        time.sleep(self.time)
        self.new_pw()
        time.sleep(self.time)
        self.hard_pw()
        time.sleep(self.time)
        self.turn_off()
