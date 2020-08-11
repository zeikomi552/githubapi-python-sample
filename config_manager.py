import json
import os

class confg_manager:

    _file_path = ".\\config\\setting.cnf"
    _conf_json = {}

    def save(self, user_name, password):
        data = {}
        data['user_param'] = []
        data['user_param'].append({
            "USERNAME": user_name,
            "PASSWORD": password
            })

        # create directory
        os.makedirs(".\\config", exist_ok=True)

        with open(self._file_path, 'w+') as outfile:
            json.dump(data, outfile)

    def load(self):

        # check exist file
        if os.path.exists(self._file_path):

            # oprn json file
            with open(self._file_path, "r") as json_file:

                # load jason data
                json_data = json.load(json_file)

                # set member parameter
                self._conf_json = json_data

        else:
            self.save("","") # Empty data Save

            self.load() # Load

    def get_userparam(self):

        return self._conf_json['user_param'][0]['USERNAME'], self._conf_json['user_param'][0]['PASSWORD']
