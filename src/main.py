# Libraries
import requests
import json
import pandas as pd
import pprint
import os
import re
import config_manager as cnf
import github_api.github_api_manager as g_api_ex

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

    # create github api object
    g_api_mn = g_api_ex.github_api_manager(username, userpassword)
    tmp = g_api_mn.get_user()

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(tmp)


if __name__ == '__main__':
    main_func()