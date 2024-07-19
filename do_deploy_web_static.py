#!/usr/bin/python3
"""
'2-do_deploy_web_static': Python script Fabrics a '.tgz archive' file off of
 the web_static directory and distributes it to web servers.
"""
from datetime import datetime
from fabric.api import local, run, put
from os.path import exists


def do_pack():
    """Creates a tap archive file aka tar.

    Args:
        None.
    Return:
        The path to the created .tgz archive or None if error.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return (None)

def do_deploy(archive_path):
    """Distributes an archive file to web servers.

    Args:
        archive_path: Directory path to the distribution archive.
    Return:
        False if the archive path doesn't exist or an error occured.
    """

    if exists(archive_path) is False:
        return (False)
    try:
        c1 = Connection("web-01", "ubuntu")
        c2 = Connection("web-02", "ubuntu")

        c1.put(archive_path, "/tmp/")
        c1.run("sudo tar -xzvf {}".format(archive_path))
        c1.run("sudo rm {}".format(archive_path))
        c1.run("sudo rm -r /data/web_static/current")
        c1.run("sudo ln -s {}{} {}".format('/data/web_static/releases/',
                                           archive_path,
                                           '/data/web_static/current')
        )

        c2.put(archive_path, "/tmp/")
        c2.run("tar -xzvf {}".format(archive_path))
        c2.run("sudo rm {}".format(archive_path))
        c2.run("sudo rm -r /data/web_static/current")
        c2.run("sudo ln -s {}{} {}".format('/data/web_static/releases/',
                                           archive_path,
                                           '/data/web_static/current')
        )

        return (True)
    except Exception:
        return (False)
