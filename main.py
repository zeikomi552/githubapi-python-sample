# Libraries
import requests
import json
import pandas as pd
import pprint
import os
import re
import github_api_test as g_api

# parameters
USERNAME = 'xxxxxxx' # github username
PASSWORD = 'xxxxxxx'  # github password
RESULT_FOLDER = 'api_result' # resuls folder path
API_V3 = 'https://api.github.com'
API_V3_FILE_NAME = "api.github.com"

# move current directory 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main_func():

    # create directory
    os.makedirs(RESULT_FOLDER, exist_ok=True)

    # init class object
    g_api_class = g_api.github_api_sample(USERNAME, PASSWORD)
    g_api_class.init_api_v3_json()

    # save api v3 json
    g_api_class.save_api_v3_json(RESULT_FOLDER)

    # request api v3
    g_api_class.save_api_v3_json_no_param(RESULT_FOLDER)

if __name__ == '__main__':
    main_func()