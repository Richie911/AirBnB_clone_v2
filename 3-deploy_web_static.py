#!/usr/bin/python3
"""
script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ['18.233.63.234','3.83.18.150']


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = 'versions/web_static_{}.tgz'.format(date)
        if os.path.isdir("versions") is False:
            local("sudo mkdir -p versions")
        local("sudo tar -czvf {} -C web_static .".format(archive_name))
        print(archive_name)
        return archive_name
    except:
        return None
def do_deploy(archive_path):
    """
        Deploy an archive to the web servers.

        :param archive_path: (str) Path to the archive file to deploy.
        :return: True if deployment is successful, False otherwise.
    """

    # Check if the archive file exists
    if not os.path.exists(archive_path):
        print(f"Error: Archive file {archive_path} not found.")
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Get the filename without extension from the archive_path
        archive_filename = os.path.basename(archive_path).split('.')[0]

        # Create the folder for the new version
        run('sudo mkdir -p /data/web_static/releases/{}'.format(archive_filename))

        # Uncompress the archive to the folder on the web server
        run('sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(
            archive_filename, archive_filename))

        # Delete the archive from the web server
        run('sudo rm /tmp/{}.tgz'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current from the web server
        run('sudo rm -rf /data/web_static/current')

        # Create a new symbolic link linked to the new version of your code
        run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_filename))

        print('New version deployed!')
        return True
    except Exception as e:
        print(f"Error deploying archive: {e}")
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
