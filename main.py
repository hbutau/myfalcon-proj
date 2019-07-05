import logging

from falcon import API

logging.basicConfig(filename='myproject.log', level=logging.DEBUG)
logger = logging.getLogger()

class APP(API):
    """This class is the main entry point into a Falcon-based app."""

    def __init__(self, *args, **kwargs):
        logger.info('****STARTING THE FALCON SERVER****')
        super().__init__(*args, **kwargs)
            # self._sinks = []
            # self._media_type = media_type
            # self._static_routes = []

            # # set middleware
            # self._middleware = helpers.prepare_middleware(
            #     middleware, independent_middleware=independent_middleware)
            # self._independent_middleware = independent_middleware

            # self._router = router or routing.DefaultRouter()
            # self._router_search = self._router.find

            # self._request_type = request_type
            # self._response_type = response_type

            # self._error_handlers = []
            # self._serialize_error = helpers.default_serialize_error

            # self.req_options = RequestOptions()
            # self.resp_options = ResponseOptions()

            # self.req_options.default_media_type = media_type
            # self.resp_options.default_media_type = media_type

            # # NOTE(kgriffs): Add default error handlers
            # self.add_error_handler(falcon.HTTPError, self._http_error_handler)
            # self.add_error_handler(falcon.HTTPStatus, self._http_status_handler)
