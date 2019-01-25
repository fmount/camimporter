Camera Photo Importer
=====================
[![Build Status](https://copr.fedorainfracloud.org/coprs/fmount/photo-importer/package/camimporter/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/fmount/photo-importer/package/camimporter/status_image/last_build.png)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](https://img.shields.io/badge/license-MIT-yellow.svg)

This is a python utility useful to import photos from your camera.
The default behavior is defined in a json configuration file and an example
of policy is like the following:


	{
		"globals": {
			"ingress": "~/Pictures/CANON/DCIM/100CANON",
			"egress": "~/Pictures/output",
			"retry": "/tmp/images.retry",
			"deep": "month"
		},
		"statistics": {
			"header": [
					"transferred",
					"skipped",
					"blacklisted",
					"failed",
					"total",
					"manually"
			]
		},
		"format": {
			"allowed": [
					"JPG",
					"jpg",
					"jpeg",
					"png",
					"raw"
			],
			"excluded": [
					"mp4",
					"avi",
					"jpg_",
					"png_",
					"rar"
			]
		}
	}

The nice feature of using a configuration like this is that a user can instruct
application to define what it has to include/exclude from the import. It also defines
the src (ingress) and dest (egress) locations and the mode to catalog the images (month,
day, year are strings allowed).

If you clone this repo, the example configuration file can be found at:

	~/path/to/clone/camimporter/config/parameters.json

or in your installation path of the python module.

Installation
---

If you are an Arch user, you can find this package on [aur](https://aur.archlinux.org/packages/camimporter)
or you can manually install this package using the Makefile provided.

	git clone https://github.com/fmount/camimporter /path/to/clone

	cd /path/to/clone

	make install  //It can also install all the required dependencies


How it works
---

This package provides a cli to run the import:

    usage camimporter -c config -i ingress_path -o egress_path -d depth -r path_retry

    Options:
      -h, --help  show this help message and exit
      -i INGRESS  path dir that contains a picture list to import
      -o EGRESS   path dir in which all imported pictures are placed
      -d DEPTH    type of grouping /by day - by month - by year
      -r RETRY    where store all failed import transactions
      -v          Print all statement during the algorithm execution
      -c CONFIG   config file to load all default config parameters.  Example file
                  can be found /usr/lib/python2.7/site-
                  packages/camimporter/config/parameters.json


Note that if you don't install the package, you can simply clone the repo, go inside
the /path/to/clone/camimporter and launch the same command in this way:

	python cli.py -c config -i ingress_path -o egress_path -d depth -r path_retry


License
---
It is distruibuted according to the [MIT License](https://github.com/fmount/camimporter/blob/master/LICENSE)
