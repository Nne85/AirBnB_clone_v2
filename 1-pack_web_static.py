#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns the path of the archive if it was successfully generated, None otherwise.
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(now)

    # Create the versions folder if it doesn't exist
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Generate the archive using tar
    result = local('tar -cvzf {} web_static'.format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path
