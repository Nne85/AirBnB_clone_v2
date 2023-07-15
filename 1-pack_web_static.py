#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    filedate = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filedate))

        return "versions/web_static_{}.tgz".format(filedate)

    except Exception as e:
        return None
