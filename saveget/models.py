from peewee import *

db = SqliteDatabase('linktag.db')

class SavedLinkTag(Model):
    url = CharField(unique=True)
    tag = CharField(unique=True)

    class Meta:
        database = db

db.connect()
db.create_tables([SavedLinkTag])
