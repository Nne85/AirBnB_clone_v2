#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os
import shlex
from datetime import datetime
from fabric.api import *

env.hosts = ["100.25.192.12", "100.25.22.89"]
env.user = "ubuntu"


@runs_once
def do_pack():
    """
    Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo.
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    present_time = strftime("%Y%M%d%H%M%S")
    output = "versions/web_static_{}.tgz".format(present_time)
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.isfile(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        rmv_ext = filename.split(".")[0]
        path_rmv_ext = "/data/web_static/releases/{}/".format(rmv_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        sudo("mkdir -p {}".format(path_rmv_ext))
        sudo("tar -xzf /tmp/{} -C {}".format(filename, path_rmv_ext))
        sudo("rm /tmp/{}".format(filename))
        sudo("mv {}web_static/* {}".format(path_rmv_ext, path_rmv_ext))
        sudo("rm -rf {}web_static".format(path_rmv_ext))
        sudo("rm -rf {}".format(symlink))
        sudo("ln -s {} {}".format(path_rmv_ext, symlink))
        print("New version deployed!")
        return True
    except Exception:
        return False
