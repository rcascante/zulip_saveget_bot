# See readme.md for instructions on running this code.

import requests
from typing import Dict, Any, Tuple, Union
from savegetclass import SaveGetData
import sched, time
from datetime import datetime

class SaveGetHandler(object):
    def usage(self) -> str:
        return '''
    Hi, I am SaveGetBot 😎, people generally give me the next orders:  save your-url the-tag | get the tag
        '''

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
        msg = message['content']
        msg_lowercase = msg.lower()
        if 'save' in msg_lowercase:
            msg_save = msg_lowercase.split(' ',2)
            if len(msg_save) > 1:
                data = SaveGetData()
                reply = data.save_data(link=msg_save[1], tag=msg_save[2])
            else:
                reply = "You need to indicate [save] [url] [tag]"

        elif 'get' in msg_lowercase:
            msg_get = msg_lowercase.split(' ',1)
            if len(msg_get) > 1:
                data = SaveGetData()
                print(data)
                reply = data.get_data(tag=msg_get[1])
            else:
                reply = "You need to indicate [save] [tag]"

        else:
            reply = self.usage()
                
        bot_handler.send_reply(message, reply)       
        
handler_class = SaveGetHandler
