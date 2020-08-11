import requests
import json
import pandas as pd
import pprint
import re

class github_api_manager:

    def __init__(self, user_name, password): 
        """ constractor 

        Args:
            user_name (str): [github user name]
            password (str): [git hub user password]
        """
        self.user_name = user_name
        self.password = password


    def get_api_json(self, base_url):
        """ request and get json file

        Args:
            base_url (str): [base url for github api v3]

        Returns:
            [JSON object]: [result]
        """
        # 1. create url text
        url = base_url # base url

        # 2. create session
        session = requests.Session()
        session.auth = (self.user_name, self.password)

        print('GET ' + url)
        # 3. GET request
        response = session.get(url)

        # return json
        return response.json()

    def get_user(self):

        base_url = "https://api.github.com/user"

        return self.get_api_json(base_url)

    def get_users(self, username = ""):

        if username == "":
            base_url = "https://api.github.com/users"
        else:
            base_url = "https://api.github.com/users/{0}".format(username)

        return self.get_api_json(base_url)