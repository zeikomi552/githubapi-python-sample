# Libraries
import requests
import json
import pandas as pd
import pprint
import os
import re
import github_api_test as g_api
import config_manager as cnf

# parameters
RESULT_FOLDER = 'api_result' # resuls folder path

# move current directory 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main_func():

    # create directory
    os.makedirs(RESULT_FOLDER, exist_ok=True)

    # load config file
    cnf_data = cnf.confg_manager()
    cnf_data.load()
    username, userpassword = cnf_data.get_userparam()

    # init class object
    g_api_class = g_api.github_api_sample(username, userpassword)
    g_api_class.init_api_v3_json()

    # save api v3 json
    g_api_class.save_api_v3_json(RESULT_FOLDER)

    # request api v3
    g_api_class.save_api_v3_json_no_param(RESULT_FOLDER)

if __name__ == '__main__':
    main_func()