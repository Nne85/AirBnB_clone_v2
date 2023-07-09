#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["100.25.192.12", "100.25.22.89"]


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    Returns True if all operations have been done correctly, otherwise returns False.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_extension = archive_filename.split('.')[0]
        tmp_path = "/tmp/{}".format(archive_filename)
        releases_path = "/data/web_static/releases/{}/".format(archive_no_extension)

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, tmp_path)

        # Uncompress the archive to the releases folder
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))

        # Move the contents of the web_static folder one level up
        run("mv {}web_static/* {}".format(releases_path, releases_path))

        # Remove the now empty web_static folder
        run("rm -rf {}web_static".format(releases_path))

        # Delete the archive from the web server
        run("rm {}".format(tmp_path))

        # Delete the existing symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new version
        run("ln -s {} /data/web_static/current".format(releases_path))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
