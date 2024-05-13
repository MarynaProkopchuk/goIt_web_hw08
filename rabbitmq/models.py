from mongoengine import Document, BooleanField
from mongoengine.fields import StringField


class Contacts(Document):
    fullname = StringField()
    email = StringField()
    message = StringField()
    completed = BooleanField(default=False)
