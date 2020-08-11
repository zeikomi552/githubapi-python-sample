import src.config_manager as cfg
import pytest
import src.github_api.github_api_manager as gapi


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

    