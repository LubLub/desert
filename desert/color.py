# -*- coding: utf-8 -*-

from json import dumps
from json import loads

from numpy import reshape
from numpy import float32 as npfloat

from .helpers import pfloat
from .helpers import json_array


class rgba():
  def __init__(self, r, g, b, a=1.0):
    self.rgba = reshape([a*r , a*g, a*b, a], (1, 4)).astype(npfloat)

  def __repr__(self):
    a = self.rgba[0, 3]
    return '<rgba {:0.3f} {:0.3f} {:0.3f} {:0.3f}>'.format(
        self.rgba[0, 0]/a,
        self.rgba[0, 1]/a,
        self.rgba[0, 2]/a,
        a)

  @staticmethod
  def from_json(j):
    if isinstance(j, str):
      j = loads(j)
    data = j['_data']
    return rgba(data['r'], data['g'], data['b'], data['a'])

  def json(self):
    _rgb = list(pfloat(r) for r in list(self.rgba[0, :]))
    return dumps({
        '_type': 'rgba',
        '_data': {
            'r': _rgb[0],
            'g': _rgb[1],
            'b': _rgb[2],
            'a': _rgb[3],
            }
        })


def rgb(r, g, b, a=1.0):
  return rgba(r, g, b, a)


def white(a=1.0):
  return rgba(1, 1, 1, a)


def black(a=1.0):
  return rgba(0, 0, 0, a)

