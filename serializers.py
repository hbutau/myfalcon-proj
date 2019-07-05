from marshmallow import fields, Schema, post_load

from models import Person


class PersonSchema(Schema):
     name = fields.Str(required=True)
     age = fields.Integer(required=True)
     race = fields.Str()

     @post_load
     def create_user(self, data, **kwargs):
         return Person(**data)


# class Person:

#     def __init__(self, name, age, race):
#             """TODO: to be defined1. """
#             self.name =  name
#             self.age = age
#             self.race = race

