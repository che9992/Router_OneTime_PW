import requests

class Check:

    def get_headers(self,session):
        headers = session.request.headers
        if headers['User-Agent']:
            headers['User-Agent'] = 'Mozilla/5.0'
        return headers

    def set_login_info(self, username, password):
        payload = {'username': username, 'passwd': password }
        self.login_info = payload
        print("Created..\n --self.login_info : {} \n".format(self.login_info))

    def __init__(self, **kwargs):

        if 'url' in kwargs:
            print('Starting DDNS status check...')
            if not 'port' in kwargs:
                self.remote_port = '80'
                print('set default port = 80')
            else:
                self.remote_port = kwargs['port']

            try:
                check_session = requests.get('http://' + kwargs['url'] + ':{}'.format(self.remote_port))
                if check_session.status_code == 200:
                    print('Router DDNS is opened.')
                    self.basic_url = kwargs['url']
                    self.headers = self.get_headers(check_session)
                    print("Created..\n --self.basic_url : {} \n --self.remote_port : {} \n --self.headers : {}\n".format(self.basic_url,self.remote_port,self.headers))
                    check_session.close()

            except:
                print("Couldn't connet to Router DDNS, Make sure your router is turned on")
                print("Connection Information\n -- DDNS : '{}' \n -- Remote Port : '{}'".format(kwargs['url'], self.remote_port))
                exit()
        else:
            print('You should input DDNS url ')
            exit()

class Login:

    def __init__(self, url, remote_port, login_info, headers):
        login_url = 'http://' + url +':'+remote_port + '/sess-bin/login_handler.cgi'

        print('Trying to log in to DDNS...')
        session = requests.post(login_url,login_info,headers)
        if session.status_code == 200:
            self.session = session
        else:
            print('Failed to log in to DDNS, Make sure your auth information')
            print("Log in Information\n -- ID : '{}' \n -- PW : '{}'".format(login_info['username'],login_info['passwd']))
            exit()

        if 'nsetCookie' in str(session.content):
            print('Log in successfully')
            session = str(session.content)
            if 'nsetCookie' in session:
                result = session.find('nsetCookie')
                cookie = {'efm_session_id': session[result + 13:result + 13 + 16]}
                self.cookie = cookie
                print("Created..\n --self.cookie : {} \n --self.session\n".format(
                    self.cookie,self.session))
            else:
                print("Can't find cookie in content")
                exit()
        else:
            print('An unknown error occurred while logging into DDNS')
