#!/usr/bin/env python
# coding=utf-8

"""
test file
"""

import six

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
