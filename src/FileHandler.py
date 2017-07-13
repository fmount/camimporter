#!/usr/bin/env python
#
# version: v1.0
# author: francesco.pantano@linux.com
#

import os
import sys
import datetime
import logging
import shutil
import re
from ImageHandler import ImageHandler as ImageObject
from utils.ConsoleUtils import ANSIColors as colorize
from utils.Stats import Stats
from prettytable import PrettyTable
from collections import defaultdict


logging.basicConfig(filename='/tmp/exifimporter.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)

cc = colorize()


class FileHandler(object):
	

	def __init__(self, ingress, egress, deep, data, retry, dry_run=False, debug=True):
		
		LOG.propagate = debug
		
		try:
			if(ingress.startswith("~/")):
				ingress = os.path.expanduser(ingress)
			
			if(egress.startswith("~/")):
				egress = os.path.expanduser(egress)
				
			if(retry.startswith("~/")):
				retry = os.path.expanduser(retry)
				
			if(os.path.exists(ingress)):
				self.ingress = ingress
				LOG.debug("[FileHandler] |/ Import base dir: [%s]" % self.ingress)
				cc.s_success("[FileHandler] ", "|/ Import base dir: [%s]" % self.ingress)
			else:
				LOG.debug("[FileHandler] |x Base in mountpoint [%s] doesn't exists" % self.ingress)
				#cc.s_error("[FileHandler] |x Base in mountpoint [%s] doesn't exists" % self.ingress)
		except Exception as e:
			cc.s_error(e)

		self.egress = egress
		self.blacklist = []
		self.deep = deep
		self.dry_run = dry_run
		
		self.transferred = "transferred.files.recap"

		# Clean retry file if it exists
		if os.path.exists(retry):
			with open(retry, "w") as f:
				f.write("")
		
		self.retry = retry
		if self.isinside(self.ingress, self.egress):
			self.blacklist.append(self.egress)
		
		self.statistics = Stats(data)
		LOG.debug("[FileHandler] |/ Defining base output mountpoint as [%s] " % self.egress)
		#cc.s_success("[FileHandler] |/ Defining base output mountpoint as [%s] " % self.egress)
	

	def isinside(self, path, directory):
		path = os.path.realpath(path)
		directory = os.path.realpath(directory)
		relative = os.path.relpath(path, directory)
		return not relative.startswith(os.pardir + os.sep)


	def flist(self, excluded):
		
		tlist = [root + os.sep + fname	\
		for root, innerdirs, filelist in os.walk(self.ingress, topdown=True)\
		for fname in filelist if fname.split(".")[-1] not in excluded]
		self.statistics.total = len(tlist)
		return tlist
		

	def os_dest_path(self, dpath):
		if not os.path.exists(self.egress + dpath):
			LOG.debug("[FileHandler] |/ Creating destination point: %s" % self.egress + dpath)
			#cc.s_success("[FileHandler] ", "|/ Creating destination point: %s" % self.egress + dpath)
			os.makedirs(self.egress + dpath)
		else:
			LOG.debug("[FileHandler] |x Skipping creation path: it exists")
			#cc.s_warning("[FileHandler] |x Skipping creation path: it exists")


	def add_transferred(self, image):
		with open(self.transferred, 'a') as f:
			f.write(image + '\n')
			LOG.debug("[FileHandler] Adding  [%s] to tranferred file " % image)


	def add_manually(self, image):
		with open(self.retry, 'a') as f:
			f.write(image + "\n")
			LOG.debug("[FileHandler] Adding %s to retry file " % image)
			#cc.s_warning("[FileHandler] Adding %s to retry file " % image)


	def transfer(self, data, dpath):
		'''
		@data is the src path of the image to transfer
		@dpath is the destination path in which we need to put the image
		'''
		try:
			if not os.path.exists(self.egress + dpath + data.split("/")[-1]):
				LOG.debug("[FileHandler] |/ [%s] => [%s]" % (data, self.egress + dpath))
				#cc.s_success("[FileHandler |/ [%s] => [%s]" % (data, self.egress + dpath))
				try:
					if self.dry_run is False:
						cc.s_success("[FileHandler] ", "|/ Tranferring %s" % data)
						shutil.copy2(data, (self.egress + dpath))
						self.statistics.transferred += 1
						#self.add_transferred(data)
				except Exception:
					LOG.error("[FileHandler] |x Error transferring [%s] " % (data))
					cc.s_error("[FileHandler] |x Error transferring [%s] " % (data))
					self.statistics.failed += 1
					self.add_manually(data)
			else:
				LOG.debug("[FileHandler] |x Skipping [%s]: File exists" % (data.split("/")[-1]))
				cc.s_warning("[FileHandler] |x Skipping [%s]: File exists" % (data))
				self.statistics.skipped += 1

		except Exception as e:
			LOG.error("[FileHandler] Transfer Failed %s " % e)
			cc.s_error(e)


	def blacklisted(self, img):
		for p in self.blacklist:
			if img.startswith(os.path.abspath(p)):
				cc.s_warning("[FileHandler] |x Blacklisting image [%s]" % img)
				LOG.warning("[FileHandler]	|x Blacklisting image [%s]" % img)
				self.statistics.blacklisted += 1
				return True
		return False
		
		

	def stats(self):
		'''
		It generates a prettytable containing the
		stats about the imported images
		'''
		x = PrettyTable(self.statistics.get_header())
		x.add_row([self.statistics.skipped, self.statistics.blacklisted, \
					self.statistics.manually_move(self.retry), \
					self.statistics.transferred, \
					self.statistics.failed, \
					self.statistics.total])
		cc.s_success("=======\nSummary\n=======")
		print(x)

if __name__ == "__main__":
	pass
