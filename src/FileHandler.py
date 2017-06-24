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
from ImageHandler import ImageHandler as ImageObject
from utils.ConsoleUtils import ANSIColors as colorize
from utils.Stats import Stats
from prettytable import PrettyTable
from collections import defaultdict


logging.basicConfig(filename='/tmp/exifimporter.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)



cc = colorize()


class FileHandler(object):
	

	def __init__(self, ingress, egress, deep, data, dry_run=False, debug=True):
		
		LOG.propagate = debug
		
		try:
			if(ingress.startswith("~/")):
				ingress = os.path.expanduser(ingress)
			
			if(egress.startswith("~/")):
				egress = os.path.expanduser(egress)
				
			if(os.path.exists(ingress)):
				self.ingress = ingress
				LOG.debug("[FileHandler] |/ Import base dir: [%s]" % self.ingress)
				#cc.s_success("[FileHandler] ", "|/ Import base dir: [%s]" % self.ingress)
			else:
				LOG.debug("[FileHandler] |x Base in mountpoint [%s] doesn't exists" % self.ingress)
				#cc.s_error("[FileHandler] |x Base in mountpoint [%s] doesn't exists" % self.ingress)
		except Exception as e:
			cc.s_error(e)

		self.egress = egress
		self.blacklist = []
		self.deep = deep
		self.dry_run = dry_run

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


	def flist(self):
		
		tlist = [root + os.sep + fname	\
		for root, innerdirs, filelist in os.walk(self.ingress, topdown=True)\
		for fname in filelist]
		
		self.statistics.total = len(tlist)
		return tlist
		

	def os_dest_path(self, dpath):
		if not os.path.exists(self.egress + dpath):
			LOG.debug("[FileHandler] |/ Creating destination point: %s" % self.egress + dpath)
			#cc.s_success("[FileHandler] ", "|/ Creating destination point: %s" % self.egress + dpath)
			os.makedirs(self.egress + dpath)
		else:
			LOG.warning("[FileHandler] |x Skipping creation path: it exists")
			#cc.s_warning("[FileHandler] |x Skipping creation path: it exists")


	def transfer(self, data, dpath):
		'''
		@data is the src path of the image to transfer
		@dpath is the destination path in which we need to put the image
		'''
		try:
			print(self.egress + dpath + data.split("/")[-1])
			print(os.path.exists(self.egress + dpath + data.split("/")[-1]))
			if not os.path.exists(self.egress + dpath + data.split("/")[-1]):
				LOG.debug("[FileHandler (DRY_RUN: %s)] |/ [%s] => [%s]" % (str(self.dry_run), data, self.egress + dpath))
				#cc.s_success("[FileHandler (DRY_RUN: %s)] ", " |/ [%s] => [%s]" % (str(self.dry_run), data, self.egress + dpath))
				try:
					if self.dry_run is False:
						cc.s_success("[FileHandler] ", "|/ Tranferring %s" % data)
						shutil.copy2(data, (self.egress + dpath))
						self.statistics.transferred += 1
				except Exception:
					LOG.s_error("[FileHandler] |x Error transferring [%s] " % (data))
					#cc.s_error("[FileHandler] |x Error transferring [%s] " % (data))
					self.statistics.failed += 1
			else:
				LOG.warning("[FileHandler] |x Skipping [%s]: File exists" % (data.split("/")[-1]))
				cc.s_warning("[FileHandler] |x Skipping [%s]: File exists" % (data.split("/")[-1]))
				self.statistics.skipped += 1

		except Exception as e:
			LOG.error("[FileHandler] Transfer Failed %s " % e)
			#cc.s_error(e)


	def blacklisted(self, img):
		for p in self.blacklist:
			if img.startswith(os.path.abspath(p)):
				#cc.s_success("[FileHandler] ", " |x Blacklisting image [%s]" % img)
				self.statistics.blacklisted += 1
				return True
		return False
		
		

	def stats(self):
		'''
		It generates a prettytable containing the
		stats about the imported images
		'''
		x = PrettyTable(self.statistics.get_header())
		x.add_row([self.statistics.total, \
		self.statistics.failed, self.statistics.skipped, \
		self.statistics.transferred, self.statistics.blacklisted])
		print(x)


if __name__ == "__main__":
	f = FileHandler("/home/fmount/Pictures", "/home/fmount/Pictures/mytest", "month")
	for im in f.flist():
		if not f.blacklisted(im):
			LOG.debug("[FileHandler] |/ Analyzing image [%s] " % im)
			#cc.s_success("[FileHandler] ", "|/ Analyzing image [%s] " % im)
			next_img = ImageObject(im, f.deep)
			if next_img.reference:
				LOG.debug("[FileHandler] |/ Building [%s] " % (f.egress + next_img.dpath))
				#cc.s_success("[FileHandler] ", "|/ Building [%s] " % (f.egress + next_img.dpath))
				f.os_dest_path(next_img.dpath)
				#print("[FileHandler] |/ Processing Image [%s] " % im)
			else:
				LOG.warning("[FileHandler] |x Skipping file [%s] " % im)
				#cc.s_warning("[FileHandler] |x Skipping file [%s] " % im)
		else:
			LOG.error("[FileHandler] |x Skipping file [%s] => BLACKLISTED " % im)
			#cc.s_error("[FileHandler] |x Skipping file [%s] => BLACKLISTED " % im)
	f.stats()
