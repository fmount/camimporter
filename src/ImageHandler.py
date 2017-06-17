#!/usr/bin/env python

from PIL import Image
from PIL.ExifTags import TAGS
from utils.ConsoleUtils import ANSIColors as colorize
import os
import pprint
import datetime
import logging

logging.basicConfig(filename='/tmp/exifimporter.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)

cc = colorize()

group_by = ["year", "month", "day"]


class ImageHandler(object):


    #def __init__(self, path, deep):
    def __init__(self, path):
        # Check path and select image type / destination
        self.ingress = path
        #for d in group_by:
        #    if deep == d:
        #        self.deep = deep

        #lambda x: self.deep = deep if

        self.reference = self.init_image()

    def init_image(self):
        self.meta = {}
        '''
        Populate image metadata using exiftools
        '''
        try:
            img = Image.open(self.ingress)
            info = img._getexif()
        except Exception:
            return False

        self.format = img.format
        self.basename = self.basename()

        if self.format is 'PNG' or info is None:
            LOG.debug("|-> [ImageHandler] Cannot process [%s], do it manually" % self.basename)
            cc.s_error("|-> [ImageHandler] Cannot process [%s], do it manually" % self.basename)
            return False

        # Exif Section to build properties
        for (tag, value) in info.items():
            decoded = TAGS.get(tag, tag)
            self.meta[decoded] = value

        self.dpath = self.gen_destination_path()

        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(self.meta)
        return True

    def basename(self):
        ptmp = self.ingress.split("/")
        if(ptmp[len(ptmp) - 1] is not "/"):
            return ptmp[len(ptmp) - 1].split(".")[0]


    def get_path(self):
        return self.ingress


    def __repr__(self):
        return "{ in: " + self.ingress + ", basename: " + self.basename + ", destination: " + self.dpath + " }"


    def gen_destination_path(self):
        default_format = "%Y:%m:%d %H:%M:%S"
        d = datetime.datetime.strptime(self.meta['DateTime'], default_format)
        dpath = "/" + "/".join([str(d.year), str(d.month), str(d.day)])
        LOG.info("[PATH] mountpoint => %s " % dpath)
        if dpath[-1] is not "/":
            dpath = dpath + "/"
        return dpath

if __name__ == "__main__":
    img = ImageHandler("/home/fmount/Pictures/IMG_20161001_164347.jpg")
    img.basename()
    img.gen_destination_path()
    print(img)
