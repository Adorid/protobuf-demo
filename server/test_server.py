#!/usr/bin/env python
# coding=utf-8

"""
test file
"""

import json
import six

from google.protobuf import json_format     # pylint: disable=no-name-in-module

from . import service_pb2


def test_GetWeatherRequest():
    req = service_pb2.GetWeatherRequest()
    assert req.city == ""
    assert req.days == 0

    req = service_pb2.GetWeatherRequest()
    req.city = "Austin"
    req.days = 3
    assert req.city == "Austin"
    assert req.days == 3


def test_GetWeatherResponse():
    rsp = service_pb2.GetWeatherResponse()
    assert len(rsp.weatherinfo) == 0

    wi = rsp.weatherinfo.add()
    wi.city = "Austin"
    wi.date = "2017-04-08"
    wi.temperature_low = 50
    wi.temperature_high = 60
    wi.wind = 10
    wi.humidity = 50
    assert len(rsp.weatherinfo) == 1
    assert rsp.weatherinfo[0].wind == 10


def test_encode_decode():
    src = service_pb2.GetWeatherRequest()
    src.city = "Austin"
    src.days = 3

    encode_result = src.SerializeToString()
    assert type(encode_result) is six.binary_type

    dst = service_pb2.GetWeatherRequest()
    dst.ParseFromString(encode_result)
    assert dst.city == src.city
    assert dst.days == src.days


def test_to_json():
    req = service_pb2.GetWeatherRequest()
    req.city = "Austin"
    req.days = 3

    json_string = json_format.MessageToJson(req)
    obj = json.loads(json_string)
    assert obj['city'] == 'Austin'
    assert obj['days'] == 3


def test_to_json_include_default_value():
    req = service_pb2.GetWeatherRequest()
    json_string = json_format.MessageToJson(req, True)
    obj = json.loads(json_string)
    assert obj['city'] == ''
    assert obj['days'] == 0


def test_from_json():
    obj = {
        'city': 'Austin',
        'days': 3,
    }
    json_string = json.dumps(obj)
    req = json_format.Parse(json_string, service_pb2.GetWeatherRequest())
    assert req.city == 'Austin'
    assert req.days == 3


def test_from_json_some_fields_missing():
    obj = {
        'city': 'Austin',
    }
    json_string = json.dumps(obj)
    req = json_format.Parse(json_string, service_pb2.GetWeatherRequest())
    assert req.city == 'Austin'
    assert req.days == 0


def test_from_json_ignore_unknown_fields():
    obj = {
        'city': 'Austin',
        'days': 3,
        'time': '07:00',
    }
    json_string = json.dumps(obj)
    req = json_format.Parse(json_string, service_pb2.GetWeatherRequest(), True)
    assert req.city == 'Austin'
    assert req.days == 3
