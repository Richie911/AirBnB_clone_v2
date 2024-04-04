#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder
    """
    try:
        # Create the versions folder if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Create the archive name based on current date and time
        now = datetime.now()
        archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)

        # Compress the web_static folder into the archive
        local("tar -czvf {} web_static".format(archive_name))

        return archive_name
    except Exception as e:
        return None
