#!/usr/bin/env python
# coding=utf-8

"""
module/program document
"""

import os
import json
import logging

from bottle import (get, post, put, route, run, request, response,
                    jinja2_template, redirect, abort,
                    default_app, debug, static_file)
import bottle

from yygame.utils import (ok, error, to_json)

from google.protobuf.text_format import MessageToString                  # pylint: disable=E0611,E0401
import service_pb2


logging.basicConfig(format='%(levelname)-8s %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def json_response(obj):
    """return a json response.

    By default, bottle only convert dict to json response automatically. This
    function converts any python object.

    Args:
        obj: any python object

    """
    response.set_header("Content-Type", "application/json")
    return to_json(obj)


def binary_response(obj):
    """return a binary response.

    Args:
        obj: should be a byte string.

    """
    response.set_header("Content-Type", "application/octet-stream")
    return obj


@get("/")
def home():
    return ok()


@post("/weather")
def get_weather():
    body = request.body
    req = service_pb2.GetWeatherRequest()
    req.ParseFromString(body.read())    # pylint: disable=no-member
    logger.info("request is:\n%s", req)

    logger.info("req.realtime=%s", req.realtime)

    r = service_pb2.GetWeatherResponse()
    wi = r.weatherinfo.add()
    wi.city = req.city
    wi.date = "2017-04-08"
    wi.temperature_low = 57
    wi.temperature_high = 67
    wi.wind = 10
    wi.humidity = 72

    wi = r.weatherinfo.add()
    wi.city = req.city
    wi.date = "2017-04-09"
    wi.temperature_low = 58
    wi.temperature_high = 68
    wi.wind = 12
    wi.humidity = 80

    return binary_response(r.SerializeToString())


@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


application = default_app()


def main():
    testing = (os.getenv("TESTING") == "yes" or
               os.getenv("DEBUG") == "1")
    port = int(os.getenv("PORT") or "8082")

    if testing:
        debug(True)
        run(app=application,
            host='localhost', port=port,
            reloader=True, quiet=False)
    else:
        run(app=application,
            server='cherrypy',
            host='127.0.0.1', port=port,
            reloader=False, quiet=True)


if __name__ == '__main__':
    main()
