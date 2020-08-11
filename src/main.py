# Libraries
import requests
import json
import pandas as pd
import pprint
import os
import re
import config_manager as cnf
import github_api.github_api_manager as gapi

# parameters
RESULT_FOLDER = 'api_result' # resuls folder path

# move current directory 
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main_func():

    owner = "microsoft"
    repo = "vscode"

    # create directory
    os.makedirs(RESULT_FOLDER, exist_ok=True)

    # load config file
    cnf_data = cnf.confg_manager()
    cnf_data.load()
    username, userpassword = cnf_data.get_userparam()

    # create github api object
    github_api = gapi.github_api_manager(username, userpassword)

    api = "/repos/{owner}/{repo}".replace("{owner}", owner).replace("{repo}", repo)

    ret_json = github_api.get_json(api)

    print(type(ret_json))
    print(ret_json.keys())

    name = ret_json.get("name")

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(ret_json)


if __name__ == '__main__':
    main_func()