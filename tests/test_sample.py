import src.config_manager as cfg
import pytest
import src.github_api.github_api_manager as gapi
import pprint

class TestClass:

    @pytest.mark.parametrize(
        "in_username, in_password",
        [
            ("test_username","test_password"),
            ("","")
        ]
    )
    def test_config(self, in_username, in_password):

        check = cfg.confg_manager()
        check.save(in_username, in_password)
        check.load()
        user_name, password = check.get_userparam()

        if (in_username == user_name) & (in_password == password):
            assert True
        else:
            assert False

    def test_api_user(self):
        cnf = cfg.confg_manager()
        cnf.load()
        username, password = cnf.get_userparam()
        check = gapi.github_api_manager(username, password)
        check.get_user()


    def test_api_user_test1(self):
        cnf = cfg.confg_manager()
        cnf.load()
        username, password = cnf.get_userparam()
        check = gapi.github_api_manager(username, password)
        json_data = check.get_user()
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(json_data) 

    def test_api_users(self):
        cnf = cfg.confg_manager()
        cnf.load()
        username, password = cnf.get_userparam()
        check = gapi.github_api_manager(username, password)
        check.get_users()
 
    @pytest.mark.parametrize("in_username",
        ("zeikomi552","microsoft")
    )
    def test_api_users2(self, in_username):
        cnf = cfg.confg_manager()
        cnf.load()
        username, password = cnf.get_userparam()
        check = gapi.github_api_manager(username, password)
        json_data = check.get_users(in_username)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(json_data) 