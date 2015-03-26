# coding: utf-8

import collections

class Tagging(object):
        __slots__ = ("tag", "obj")
        def __init__(self, tag, obj):
            self.tag = tag
            self.obj = obj
        def __eq__(self, other):
            return isinstance(other, Tagging) and self.tag == other.tag and self.obj == other.obj
        def __hash__(self):
            return hash((self.tag, self.obj))

class _Undefined(object):
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __str__(self):
		return "Undefined"

	def __repr__(self):
		return "Undefined"

Undefined = _Undefined()
