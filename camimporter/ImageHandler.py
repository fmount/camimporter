# -*- coding: utf-8 -*-

############################################################################
#
#       Licensed under the MIT License (the "License"); you may not use this file
#       except in compliance with the License.  You may obtain a copy of the License
#       in the LICENSE file or at
#
#           https://opensource.org/licenses/MIT
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#    author: fmount <fmount9@autistici.org>
#    version: 0.1
#    company: --
#
#############################################################################

from PIL import Image
from PIL.ExifTags import TAGS
from utils.ConsoleUtils import ANSIColors as colorize
import os
import six
import pprint
import datetime
import logging
import unicodedata

logging.basicConfig(filename='/tmp/exifimporter.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)

cc = colorize()

group_by = ["year", "month", "day"]
months =    {   1: "January", \
                2: "February", \
                3: "March", \
                4: "April", \
                5: "May", \
                6: "June", \
                7: "July", \
                8: "August", \
                9: "September", \
                10: "October", \
                11: "November", \
                12: "December"
            }


class ImageHandler(object):


    def __init__(self, path, deep, allowed, debug=True):
        # Check path and select image type / destination
        
        LOG.propagate = debug

        self.ingress = path
        self.allowed = allowed
        self.deep = self.deep(deep)
        self.reference = self.init_image(self.ingress)

    #TODO: Make this part more elegant
    #self.deep = filter(lambda x, y: True if x == y else False, group_by)
    def deep(self, deep):
        for d in group_by:
            if deep == d:
                return d
        return group_by[2]


    def is_allowed(self, ext):
        return True if ext in self.allowed else False


    def init_image(self, ingress):
        
        '''
        Populate image metadata using exiftools
        only if the ext is allowed;
        N.B.
        Remember that this function make your image
        pass ONLY if the extention is explicitely 
        ALLOWED: I block everything is not explicitely
        allowed.
        '''
        self.meta = {}

        if self.is_allowed(ingress.split(".")[-1]):
            try:
                img = Image.open(self.ingress)
                info = img._getexif()
            except Exception:
                return False

            self.format = img.format
            self.basename = self.basename()
            
            if self.format is 'PNG' or info is None:
                #LOG.debug("|-> [ImageHandler] Cannot process [%s], do it manually" % self.basename)
                cc.s_error("|-> [ImageHandler] Cannot process [%s], do it manually" % self.basename)
                return False

            # Exif Section to build properties
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                self.meta[decoded] = value
                
            if(self.meta.get("DateTime", None) is None):
                print("DateTime not present")
                return False

            if (self.meta["DateTime"].startswith("\x00")):
                print("DateTime format is not valid!")
                return False

            self.dpath = self.gen_destination_path()
            return True
        return False

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
        if(six.PY2):
            d = datetime.datetime.strptime(self.meta.get('DateTime', \
                                       '0000:00:00 00:00:00').decode('ascii'), \
                                        default_format.decode('ascii'))
        else:
            d = datetime.datetime.strptime(self.meta.get('DateTime', \
                                            '0000:00:00 00:00:00'), \
                                            default_format)
        if self.deep == "day":
            dpath = "/" + "/".join([str(d.year), months[d.month], str(d.day)])
        elif self.deep == "month":
            dpath = "/" + "/".join([str(d.year), months[d.month]])
        else:
            dpath = "/" + "/".join([str(d.year)])

        LOG.info("[PATH] mountpoint => %s " % dpath)
        if dpath[-1] is not "/":
            dpath = dpath + "/"
        return dpath


'''
if __name__ == "__main__":
    img = ImageHandler("~/Pictures/IMG_20161001_164347.jpg", "month")
    #img.basename()
    img.gen_destination_path()
    print(img)
'''
