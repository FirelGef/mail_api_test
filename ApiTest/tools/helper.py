import requests

from cfg.prod_conf import *


class Helper:
    login: str
    domain: str
    password: str

    def __init__(self):
        self.helper = None

    @classmethod
    def setup_helper(self, login, domain, password):
        # Create session

        with requests.Session() as session:
            # auth
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
            session.post(url=f'{protocol}://{auth_farm}/cgi-bin/auth?',
                         data={'Login': login,
                               'Domain': domain,
                               'Password': password,
                               'saveauth': 1},
                         headers=headers,
                         verify=True)
            # get token
            token_response = session.get(f'{protocol}://{farm}/api/v1/tokens?email={login}@{domain}')

            if token_response.json()['status'] != 200:
                raise RuntimeError(f'Failed to get token. tokens response: {token_response.json()}')

            session.token = token_response.json()['body']['token']
            session.email = f'{login}@{domain}'
            self.helper = session

            return self.helper

    @classmethod
    def send_api_request(self, endpoint, **kwargs):
        requests_params = f'token={self.helper.token}&email={self.helper.email}'
        for key in kwargs.keys():
            requests_params += f'&{key}={kwargs[key]}'

        response = self.helper.get(f'{protocol}://{farm}/api/v1/{endpoint}?{requests_params}')

        if response.status_code != 200:
            raise RuntimeError(
                f'Failed to get {endpoint}. {response.status_code} status_code: {response.status_code}, text: {response.text}'
            )

        return response.json()
