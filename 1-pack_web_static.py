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

        # Get the current date and time as a string
        date_time_str = datetime.now().strftime('%Y%m%d%H%M%S')

        # Create the archive name based on current date and time
        archive_name = f'versions/web_static_{date_time_str}.tgz'

        # Compress the web_static folder into the archive
        local("tar -czvf {} web_static".format(archive_name))

        return archive_name
    except Exception as e:
        return None
