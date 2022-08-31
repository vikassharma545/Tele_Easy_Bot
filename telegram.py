import requests

class telegram:

    __access_token = ''
    __base_url = f"https://api.telegram.org/bot{__access_token}"   

    def __init__(self, access_token):
        self.__access_token = access_token
             
    def get_Updates(self):
        """ Get Update """
        url = f"{self.base_url}/getUpdates"
        return requests.post(url)

    