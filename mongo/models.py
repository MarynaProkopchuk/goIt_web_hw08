from mongoengine import Document, CASCADE
from mongoengine.fields import (
    ReferenceField,
    ListField,
    StringField,
)


class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField()
