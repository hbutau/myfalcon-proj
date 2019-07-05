import json
import logging

import falcon
from marshmallow import Schema
from marshmallow.exceptions import ValidationError

from serializers import PersonSchema
from models import Person
from main import APP

logging.basicConfig(filename='myproject.log', level=logging.DEBUG)
logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

person_data = {}
munhu = Person('Humphrey', 34, 'african')

class PersonResource(object):

    """Docstring for PersonResource. """


    def on_get(self, req, resp, mumhu=None):
        """TODO: Docstring for on_get.

        :param: Client's HTTP request
        :person: TODO
        :returns: TODO

        """
        # here we need to serialize person
        schema = PersonSchema()
        result = schema.dump(munhu)
        logger.info(result)
        resp.media = result
        resp.status = falcon.HTTP_200


    def on_post(self, req, res):
        # here we need to deserialize to a python object since we are recieving json from req.media
        # user_req = req.context["data"]
        # logger.info(req.stream.read())
        schema = PersonSchema()
        try:
            result = schema.load(req.media)
        except ValidationError as err:
            err.messages['name'] = "You need to supply a {}".format(err.messages.keys())
            res.media = err.messages
            res.status = falcon.HTTP_403
        # req.context.data = req.media
        # person = Person(**req.media)
        # person_data.update(user_req)
        res.status = falcon.HTTP_201


person = PersonResource()

app = APP()
app.add_route('/people', person)
