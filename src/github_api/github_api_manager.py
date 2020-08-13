import requests
import json
import pandas as pd
import pprint
import re

class github_api_manager:

    GITHUB_API = "https://api.github.com"

    def __init__(self, user_name, password): 
        """ constractor 

        Args:
            user_name (str): [github user name]
            password (str): [git hub user password]
        """
        self.user_name = user_name
        self.password = password


    def get_json(self, api, debug_log = False):
        """ request and get json file

        Args:
            api (str): [base url for github api v3]

        Returns:
            [JSON object]: [result]
        """

        # 1. create url text
        url = self.GITHUB_API + api # base url

        # return json
        return self.get_json_url(url, debug_log)

    def get_json_url(self, url, debug_log = False):
        """ request and get json file

        Args:
            api (str): [base url for github api v3]

        Returns:
            [JSON object]: [result]
        """
        # 2. create session
        session = requests.Session()
        session.auth = (self.user_name, self.password)

        if debug_log == True:
            # for debug
            print('GET ' + url)

        # 3. GET request
        response = session.get(url)

        # return json
        return response.json()