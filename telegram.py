import json
import requests
from time import sleep

class telegram:

    def __init__(self, access_token):
        """ Initialised ACCESS TOKEN """

        self.__access_token = access_token
        self.__base_url = f"https://api.telegram.org/bot{self.__access_token}"
             
    def get_Updates(self, offset=None):
        """ Get Update """
        url = f"{self.__base_url}/getUpdates?offset={offset}"
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
        files = {"photo" : open(image_path,'rb')}
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
    
    def active_bot(self, StartStopKey="vikshar", response_dict = {"hi" : "hello !!! \nI'm Vikshar, How can i help you :)"}):

        run_loop, bot_active, offset = True, False, 1
        while run_loop:
            try:
                sleep(10)
                response = self.get_Updates(offset).json()['result']

                for value in response:
                    if list(value['message'].keys())[-1] == 'text':
                        print(value)
                        
                        if value['message']['text'] == StartStopKey:
                            bot_active = True
                            group_id = value['message']['chat']['id']
                            offset = value['update_id'] + 1
                            self.send_message(group_id, message="Bot Activated...")
                            break

                        if value['message']['text'] == f"{StartStopKey} exit":
                            run_loop = False

                while bot_active:
                    sleep(2)
                    response = self.get_Updates(offset).json()['result']

                    for value in response:
                        if list(value['message'].keys())[-1] == 'text':
                            print(value)
                            
                            if value['message']['text'] in response_dict.keys():
                                self.send_message(group_id, message=response_dict[value['message']['text']])

                            if value['message']['text'] == StartStopKey:
                                bot_active = False
                                self.send_message(group_id, message="Bot Deactivated...")

                    if len(response) != 0:
                        offset = response[-1]['update_id'] + 1

            except Exception as e:
                print(e)
