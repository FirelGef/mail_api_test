import requests

from cfg.prod_conf import *

class Helper:
    @classmethod
    def setup_helper(self, login, domain, password):
        # Create session
        with requests.Session() as session:
            # auth
            session.get(
                '{0}://{1}/cgi-bin/auth?Login={2}&Domain={3}&Password={4}'.format(protocol,
                                                                                  auth_farm,
                                                                                  login,
                                                                                  domain,
                                                                                  password))
            # get token
            token_response = session.get('{0}://{1}/api/v1/tokens?email={2}@{3}'.format(protocol, farm, login, domain))

            if token_response.json()['status'] != 200:
                raise RuntimeError('Failed to get token. tokens response: {0}'.format(token_response.json()))

            session.token = token_response.json()['body']['token']
            session.email = '{0}@{1}'.format(login, domain)

        return session

    @classmethod
    def send_api_request(self, helper, endpoint, **kwargs):
        requests_params = 'token={0}&email={1}'.format(helper.token, helper.email)
        for key in kwargs.keys():
            requests_params += '&{0}={0}'.format(key, kwargs[key])

        response = helper.get('{0}://{1}/api/v1/{2}?{3}'.format(protocol, farm, endpoint, requests_params))

        if response.json()['status'] != 200:
            raise RuntimeError('Failed to get {0}. {0} response: {1}'.format(endpoint, response.json()))

        return response.json()

