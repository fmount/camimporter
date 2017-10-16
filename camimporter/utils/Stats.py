# -*- coding: utf-8 -*-

############################################################################
#
#       Licensed under the MIT License (the "License"); you may not use this file
#       except in compliance with the License.  You may obtain a copy of the License
#       in the LICENSE file or at
#
#    		https://opensource.org/licenses/MIT
#
# 	Unless required by applicable law or agreed to in writing, software
# 	distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# 	WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# 	See the License for the specific language governing permissions and
# 	limitations under the License.
#
#	 author: fmount <fmount9@autistici.org>
#	 version: 0.1
#	 company: --
#
#############################################################################

########
#
# Total files: [total - blacklisted]
#
# Total files is also given by: [manually + skipped + transferred + failed - blacklisted]
#
#######

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
        try:
            distinct = set()
            with open(fname, "r") as f:
                for line in f.readlines():
                    distinct.add(line)
            return len(distinct)
        except:
            return 0


if __name__ == "__main__":
    data = ["transferred", "skipped", "blacklisted", "failed", "total"]
    s = Stats(data)
    s.transferred = 0
    print(s)
    print(s.get_header())
