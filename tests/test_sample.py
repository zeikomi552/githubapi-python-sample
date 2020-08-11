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

        cfg.confg_manager().save(in_username, in_password)
        user_name, password = cfg.confg_manager().get_userconf()

        if (in_username == user_name) & (in_password == password):
            assert True
        else:
            assert False
