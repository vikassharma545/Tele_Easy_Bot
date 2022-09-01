import requests
import json

class telegram:
    __access_token = ''
    __base_url = ''   

    def __init__(self, access_token):
        """ Initialised ACCESS TOKEN """

        self.__access_token = access_token
        self.__base_url = f"https://api.telegram.org/bot{self.__access_token}"
             
    def get_Updates(self):
        """ Get Update """
        url = f"{self.__base_url}/getUpdates"
        return requests.post(url)

    def send_message(self, chat_id, message, disable_notification=False, protect_content=False, reply_to_message_id=0):
        """ Send message """
        url = f"{self.__base_url}/sendMessage"
        parameters = { "chat_id":chat_id, "text":message, "parse_mode":"Markdown", "disable_notification":disable_notification, "protect_content":protect_content, "reply_to_message_id":reply_to_message_id }
        return requests.post(url, params=parameters)

    def forward_message(self, chat_id, from_chat_id, message_id):
        """ Send message """
        url = f"{self.__base_url}/sendMessage"
        parameters = { "chat_id":chat_id, "from_chat_id":from_chat_id, "message_id":message_id }
        return requests.post(url, params=parameters)

    def send_image(self, chat_id, image_path, caption):
        """  Send Image from file path  """
        url = f"{self.__base_url}/sendPhoto"
        parameters = { "chat_id":chat_id, "caption":caption, "parse_mode":"Markdown" }
        files = { "photo" : open(image_path,'rb') }
        return requests.post(url, params=parameters, files=files)
        
    def send_documents(self, chat_id, file_path, caption):
        """ Send Documents """
        url = f"{self.__base_url}/sendDocument"

        parameters = {"chat_id": chat_id, "caption": caption, "parse_mode":"Markdown" }
        files = {"document": open(file_path, 'rb')}
        return  requests.post(url,params=parameters, files=files)

    def send_poll(self, group, question, option_list, is_anonymous=True, type="regular", correct_option_id=0, disable_notification=False, protect_content=False, reply_to_message_id=0):
        """" Send Poll Message """
        url = f"{self.base_url}/sendPoll"
        parameters = { "chat_id":group, "question":question,  "options":json.dumps(option_list), "is_anonymous":is_anonymous, "type":type, "correct_option_id":correct_option_id, "disable_notification":disable_notification, "protect_content":protect_content, "reply_to_message_id":reply_to_message_id}
        return requests.post(url, params=parameters)
