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

import optparse
import os
import sys
import logging
from CamImporter import CameraImporter
from utils.ConsoleUtils import ANSIColors as colorize

logging.basicConfig(filename='/tmp/exifimporter.log', level=logging.DEBUG)
LOG = logging.getLogger(__name__)

cc = colorize()

def loadconfig(*args):
    return filter((lambda x: x is not None), args)


def check_config_path(p):
    return os.path.exists(os.path.expanduser(p))


def cli():
    print("------------------------------")
    print("CAMERA IMPORT CLI TOOL")
    print("------------------------------\n")

    parser = optparse.OptionParser('\nusage %prog -c config -i ingress_path -o egress_path -d depth -r path_retry')
    parser.add_option('-i', dest='ingress', type='string', help='path dir that contains a picture list to import')
    parser.add_option('-o', dest='egress', type='string', help='path dir in which all imported pictures are placed')
    parser.add_option('-d', dest='depth', type='string', help='type of grouping /by day - by month - by year')
    parser.add_option('-r', dest='retry', type='string', help='where store all failed import transactions')
    parser.add_option('-v', action='store_true', dest='verbosity', help='Print all statement during the algorithm execution')
    parser.add_option('-c', dest='config', type='string', help='config file to load all default config parameters.\n Example file can be found /usr/lib/python2.7/site-packages/camimporter/config/parameters.json')

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

    if config is not None:
        cc.s_success("[CLI] ", "|/ Config file provided, ignoring other options")
        if(check_config_path(config)):
            c = CameraImporter(config, None, None, None, None, debug)
            c.import_objects()
        else:
            cc.s_error("[ERROR] Config file: no such file or directory! Exiting ...")
            LOG.error("[ERROR] Config file: no such file or directory! Exiting ...")
            sys.exit(-1)
    else:
        #print("You provide %s parameters" % (len(loadconfig(ingress, egress, depth, retry, debug))))
        #c = CameraImporter(None, ingress, egress, depth, retry, debug)
        #c.import_objects()
        parser.print_help()


if __name__ == '__main__':
    cli()


#######################
#  python cli.py -c config/parameters.json -v
#  python cli.py -i ~/Pictures/bacheca -o ~/Pictures/mytest -d month -v
########################
