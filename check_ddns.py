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
    def __init__(self, url, remote_port):

        print('Starting DDNS status check...')

        try:
            check_session = requests.get('http://' + url + ':{}'.format(remote_port))
            if check_session.status_code == 200:
                print('Router DDNS is opened.')
                self.basic_url = url
                self.remote_port = remote_port
                self.headers = self.get_headers(check_session)
                print("Created..\n --self.basic_url : {} \n --self.remote_port : {} \n --self.headers : {}\n".format(self.basic_url,self.remote_port,self.headers))
                check_session.close()

        except:
            print("Couldn't connet to Router DDNS, Make sure your router is turned on")
            print("Connection Information\n -- DDNS : '{}' \n -- Remote Port : '{}'".format(url, remote_port))

class Login:

    def __init__(self, url, remote_port, login_info, headers):
        login_url = 'http://' + url +':'+remote_port + '/sess-bin/login_handler.cgi'

        print('Trying to log in to DDNS...')
        session = requests.post(login_url,login_info,headers)
        self.session = session
        if 'nsetCookie' in str(session.content):
            print('Log in successfully')
            session = str(session.content)
            if 'nsetCookie' in session:
                result = session.find('nsetCookie')
                cookie = {'efm_session_id': session[result + 13:result + 13 + 16]}
                self.cookie = cookie
                print("Created..\n --self.cookie : {} \n --self.session\n".format(
                    self.cookie,self.session))

        elif 'session_timeout' in str(session.content):
            print('Failed to log in to DDNS, Make sure your auth information')
            print("Log in Information\n -- ID : '{}' \n -- PW : '{}'".format(login_info['username'],login_info['passwd']))
        else:
            print('An unknown error occurred while logging into DDNS')
