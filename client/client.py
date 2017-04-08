#!/usr/bin/env python
# coding=utf-8

"""
get weather client
"""

from __future__ import print_function, unicode_literals

import requests

from server import service_pb2


def main():
    req = service_pb2.GetWeatherRequest()
    req.city = "Austin"
    req.days = 3
    r = requests.post('http://localhost:8082/weather', req.SerializeToString())
    res = service_pb2.GetWeatherResponse()
    res.ParseFromString(r.content)
    print(res)


if __name__ == '__main__':
    main()
