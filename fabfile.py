#!/usr/bin/python3
"""This module provides a Fabric script for deploying web_static
archives to web servers.
"""
from fabric.api import env, run, put, local
from os.path import exists
from datetime import datetime

# Set the enironment variables
env.hosts = ['100.27.4.97', '100.26.254.126']
env.user = 'ubuntu'
env.key_filename = '/home/ansayong/.ssh/id_rsa'
env.password = 'boomerang'

def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Get the filename without extension
        archive_filename = archive_path.split('/')[-1][:-4]

        # Create the release folder on the web server
        run('mkdir -p /data/web_static/releases/{}'.format(archive_filename))

        # Uncompress the archive into the release folder
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
            .format(archive_path.split('/')[-1], archive_filename))

        # Remove the uploaded archive from the web server
        run('rm /tmp/{}'.format(archive_path.split('/')[-1]))

        # Move the contents to the web static folder
        run('mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'
            .format(archive_filename, archive_filenamme))

        # Remove the empty web_static folder
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_filename))

        # Delete the old symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s /data/web_static/releases/{} \
                /data/web_static/current'.format(archive_filename))

        return True

    except:
        return False
