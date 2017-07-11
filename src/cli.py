#!/usr/bin/env python

import optparse
import os
import sys
import logging
from CamImporter import CameraImporter

logging.basicConfig(filename='/tmp/exifimporter.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)


def loadconfig(*args):
	return filter((lambda x: x is not None), args)


def check_config_path(p):
	return os.path.exists(os.path.expanduser(p))


def cli():
	print("------------------------------")
	print("CAMERA IMPORT CLI TOOL")
	print("------------------------------\n")

	parser = optparse.OptionParser('\nusage %prog -i ingress_path -o egress_path -d depth -r path_retry')
	parser.add_option('-i', dest='ingress', type='string', help='path dir that contains a picture list to import')
	parser.add_option('-o', dest='egress', type='string', help='path dir in which all imported pictures are placed')
	parser.add_option('-d', dest='depth', type='string', help='type of grouping /by day - by month - by year')
	parser.add_option('-r', dest='retry', type='string', help='where store all failed import transactions')
	parser.add_option('-v', action='store_true', dest='verbosity', help='Print all statement during the algorithm execution')
	parser.add_option('-c', dest='config', type='string', help='config file to load all default config parameters')

	(options, args) = parser.parse_args()

	ingress = options.ingress
	egress = options.egress
	depth = options.depth
	retry = options.retry
	debug = options.verbosity
	config = options.config

	# Check debug mode to toggle logging
	if(debug is not None):
		LOG.propagate = True
	else:
		LOG.propagate = False

	# TODO:
	# If all parameters are None, verify that config file exists before
	# instantiate the CameraImporter object ...

	if config is not None:
		print("You provide a config file, it has priority on the other parameters")
		if check_config_path(config):
			print("RUN CAMERA IMPORTER WITH FILE CONFIG AND IGNORE ALL OTHERS PARAMETERS")
			c = CameraImporter(config, None, None, None, None, debug)
			c.import_objects()
		else:
			print("[ERROR] Config file: no such file or directory! Exiting ...")
			sys.exit(-1)
		#if len(loadconfig(ingress, egress, depth, retry, debug)) == 0:
		#print("No parameters provided, we need to check the config file")
	else:
		print("You provide %s parameters" % (len(loadconfig(ingress, egress, depth, retry, debug))))
		c = CameraImporter(None, ingress, egress, depth, retry, debug)
		c.import_objects()
	

if __name__ == '__main__':
	cli()
