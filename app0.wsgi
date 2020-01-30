#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/app0/")
sys.path.insert(0,"/var/www/app0/app0/")

import logging
logging.basicConfig(stream=sys.stderr)

from app0 import app as application
