#!/usr/bin/env python
#
# version: v1.0
# author: francesco.pantano@linux.com
#

import os
import sys
import datetime
import logging
import config
from FileHandler import FileHandler
from ImageHandler import ImageHandler as ImageObject
from utils.parser import Parser as Parser
from utils.ConsoleUtils import ANSIColors as colorize


logging.basicConfig(filename='/tmp/exifimporter.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)

cc = colorize()


# TODO:
# We have lots of issues related to basename of photos that may contains spaces, symbols or
# something else, so we need a function to normalize them before starting to analize

class CameraImporter(Parser):


	def __init__(self, conf=None, ingress=None, egress=None, \
				deep=None, retry=None, debug=True):
		
		LOG.propagate = debug
		if conf is not None:
			config.parameters_json_file_source['conf'] = conf
	
		super(CameraImporter, self).__init__(config.parameters_json_file_source)

		self.ingress = ingress
		self.egress = egress
		self.deep = deep
		self.retry = retry

		self.parse()
		

	def parse(self):
		self.configure = self.raw_json
		# Build the global attributes
		for key, value in self.configure.get("globals").items():
			if getattr(self, key, None) is None:
				setattr(self, key, value)
			LOG.debug("[CameraImporter] Acquiring attribute [%s] with default value [%s]" % (key, str(value)))
		
		self.allowed = self.configure["format"]["allowed"]
		self.excluded = self.configure["format"]["excluded"]


	def __setattr__(self, key, value):
		self.__dict__[key] = value


	def instlookup(self, name):
		True if name in self.__dict__.keys() else False

	
	def import_objects(self):
		try:
			
			f = FileHandler(self.ingress, self.egress, self.deep, \
							self.configure['statistics']['header'], self.retry, False, True)
			for im in f.flist(self.excluded):
				if not f.blacklisted(im):
					LOG.debug("[FileHandler] |/ Analyzing image [%s] " % im)
					next_img = ImageObject(im, f.deep, self.allowed)
					if next_img.reference:
						LOG.debug("[FileHandler] |/ Building [%s] " % (f.egress + next_img.dpath))
						f.os_dest_path(next_img.dpath)
						f.transfer(next_img.ingress, next_img.dpath)
					else:
						LOG.debug("[FileHandler] |x Skipping file [%s] " % im)
						cc.s_warning("[FileHandler] |x Skipping file [%s] " % im)
						f.add_manually(im)
				else:
					LOG.error("[FileHandler] |x Skipping file [%s] => BLACKLISTED " % im)
					cc.s_error("[FileHandler] |x Skipping file [%s] => BLACKLISTED " % im)
					f.add_manually(im)
			f.stats()
		except Exception as e:
			#TODO: Raise the correct exception...
			LOG.error(e)
			print(e)
