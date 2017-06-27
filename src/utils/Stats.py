#!/usr/bin/env python
#
# version: v1.0
# author: francesco.pantano@linux.com
#

import json
import sys
import logging

logging.basicConfig(filename='/tmp/exifimporter.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)


class Stats(object):


	def __init__(self, header):
		for key in header:
			setattr(self, key, 0)


	def __setattr__(self, key, value):
		self.__dict__[key] = value


	def __getattr__(self, key):
		return key


	def __repr__(self):
		for key, value in self.__dict__.items():
			print("[%s] => [%d] " % (key, value))


	def __str__(self):
		return str(json.loads(json.dumps(self.__dict__)))


	def get_header(self):
		return self.__dict__.keys()
	

	def manually_move(self, fname):
		distinct = set()
		with open(fname, "r") as f:
			for line in f.readlines():
				distinct.add(line)
		return len(distinct)


if __name__ == "__main__":
	data = ["transferred", "skipped", "blacklisted", "failed", "total"]
	s = Stats(data)
	s.transferred = 0
	print(s)
	print(s.get_header())
