#!/usr/bin/python3
"""
'1-pack_web_static' is a '.tgz archive' file creation script
written in python to run using the 'fab' command.
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Creates a tap archive file aka tar.

    Args:
        None.
    Return:
        The path to the created .tgz archive or None if error.
    """

    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

        if local("tar -cvzf {} web_static".format(file)).failed is True:
            return None
        return file
