import requests

class telegram:
    __author_public_token = "5475372934:AAElRw3sAXMAzs9nH1YkkzZ5MS2bBP4IelY"
    __access_token = ''
    __base_url = f"https://api.telegram.org/bot{__access_token}"   

    def __init__(self, access_token =__author_public_token):
        """ Initialised ACCESS TOKEN """

        self.__access_token = access_token
             
    def get_Updates(self):
        """ Get Update """
        url = f"{self.base_url}/getUpdates"
        return requests.post(url)

    def send_message(self, chat_id, message):
        """ Send message """
        url = f"{self.base_url}/sendMessage"
        parameters = { "chat_id":chat_id, "text":message, "parse_mode":"Markdown" }
        return requests.post(url, params=parameters)

    def send_image(self, chat_id, image_path, caption):
        """  Send Image from file path  """
        url = f"{self.base_url}/sendPhoto" 
        parameters = { "chat_id":chat_id, "caption":caption, "parse_mode":"Markdown" }
        files = { "photo" : open(image_path,'rb') }
        return requests.post(url, params=parameters, files=files)
        
    def send_documents(self, chat_id, file_path, caption):
        """ Send Documents """
        url = f"{self.base_url}/sendDocument"

        parameters = {"chat_id": chat_id, "caption": caption, "parse_mode":"Markdown" }
        files = {"document": open(file_path, 'rb')}
        return  requests.post(url,params=parameters, files=files)
