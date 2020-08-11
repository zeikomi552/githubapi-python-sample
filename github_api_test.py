import requests
import json
import pandas as pd
import pprint
import re

class github_api_sample:
    
    API_V3_PATH = 'https://api.github.com'

    def __init__(self, user_name, password): 
        """ constractor 

        Args:
            user_name (str): [github user name]
            password (str): [git hub user password]
        """
        self.api_v3_json = ""
        self.user_name = user_name
        self.password = password

    def init_api_v3_json(self):
        """ request api v3 and set 

        Args:
            user_name (str): [description]
            password ([type]): [description]

        Returns:
            [type]: [description]
        """
        # set json
        self.api_v3_json = self.get_api_json(github_api_sample.API_V3_PATH)

        # return test
        return self.api_v3_json

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

        # 3. GET request
        response = session.get(url)

        # return json
        return response.json()

    def save_api_v3_json(self, result_folder_path):
        """ save json file for 'https://api.github.com'

        Args:
            file_path (str): [save folder path]
        """
        
        # set save filepath for results
        file_path = result_folder_path + "/" + "api.github.com" + '.json'

        # save api v3 json file
        self.save_json(self.api_v3_json, file_path)

    def save_json(self, json_obj, file_path):
        """ save json file

        Args:
            json_obj (JSON object): [json object]
            file_path (str): [save file path]
        """

        # save json file
        with open(file_path, 'w') as outfile:
            json.dump(json_obj, outfile, indent=4)

    def save_json_object(self, base_url, file_path):
        """ request github rest api v3

        Args:
            base_url (str): [github api base url]
            file_path (str): [save file path]
        """
        # get json file
        tmp_json = self.get_api_json(base_url)

        # save file
        self.save_json(tmp_json, file_path)

    def save_api_v3_json_no_param(self, result_folder_path):
        """ save no parameter api 

        Args:
            result_folder_path (str): [output folder]
        """

        # get items
        for key, value in self.api_v3_json.items():

            # init api v3
            self.init_api_v3_json()

            # set save filepath for results
            file_path = result_folder_path + "/" + key + '.json'
            result = re.search(r"\{.*\}", value)

            # non args check
            if result is None:

                # request and save
                self.save_json_object(value, file_path)




