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


class CameraImporter(Parser):


	def __init__(self):
		super(CameraImporter, self).__init__(config.parameters_json_file_source)

	def parse(self):
		self.configure = self.raw_json

	def import_objects(self, ingress, egress):
		f = FileHandler(ingress, egress, "month", self.configure['statistics']['header'])
		for im in f.flist():
			if not f.blacklisted(im):
				LOG.debug("[FileHandler] |/ Analyzing image [%s] " % im)
				cc.s_success("[FileHandler] ", "|/ Analyzing image [%s] " % im)
				next_img = ImageObject(im, f.deep)
				if next_img.reference:
					LOG.debug("[FileHandler] |/ Building [%s] " % (f.egress + next_img.dpath))
					cc.s_success("[FileHandler] ", "|/ Building [%s] " % (f.egress + next_img.dpath))
					f.os_dest_path(next_img.dpath)
					#print("[FileHandler] |/ Processing Image [%s] " % im)
				else:
					LOG.warning("[FileHandler] |x Skipping file [%s] " % im)
					cc.s_warning("[FileHandler] |x Skipping file [%s] " % im)
			else:
				LOG.error("[FileHandler] |x Skipping file [%s] => BLACKLISTED " % im)
				cc.s_error("[FileHandler] |x Skipping file [%s] => BLACKLISTED " % im)
		f.stats()


if __name__ == "__main__":
	c = CameraImporter()
	c.parse()
	c.import_objects("/home/fmount/Pictures", "/home/fmount/Pictures/mytest")
