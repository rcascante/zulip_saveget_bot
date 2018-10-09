from models import SavedLinkTag
from peewee import *

class SaveGetData: 

    def save_data(self,link,tag):
        for data in SavedLinkTag.select():
            if link == data.url or tag == data.tag:
                return "This tag or url already exist, please try another one"
        data =  SavedLinkTag(url=link, tag=tag)
        data.save()
        return "Url {} has been saved under the tag {}".format(link, tag)
        

    def get_data(self,tag):
        for data in SavedLinkTag.select():
            if tag == data.tag:
                return  "The url with the tag {} is: {}".format(data.tag, data.url)
        return "The url with the tag {}, does not exist".format(tag)
    

    

  

