# -*- coding: utf-8 -*-

"""Default options for the application.
"""

# version
VERSION = '0.3'

# sqlite DB file
SQLITE_DB = 'db/auth.db' 

# maximum number of authorized IPs per user 
MAX_AUTH_IP_COUNT = 1000000

# automatic IP authorization without authentication
# do not set this to True, unless you *really* know what you are doing
AUTO_AUTH = True

# web debug output dump
DEBUG = False

# default web.py server port
DEFAULT_PORT = 8080

# form input mode
FORM_INPUTS_HIDDEN = False
