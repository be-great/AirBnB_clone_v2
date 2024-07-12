#!/usr/bin/python3
""" 1. Compress before sending """
from fabric.api import env, put, run, task
import os


env.hosts = ['100.25.46.0', '54.210.60.100']


def do_pack():
    """create compression file"""
    if not os.path.exists("versions"):
        os.makedirs("versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"

    # Create the archive
    try:
        local(f"tar -czvf {archive_name} web_static")
        return archive_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """ Deploy a compressed archive to the web servers. """
    if not os.path.exists(archive_path):
        return False

    try:
        arch_name = os.path.basename(archive_path)
        arch_base = os.path.splitext(arch_name)[0]

        # Upload archive to /tmp/ directory on remote server
        put(archive_path, "/tmp/")

        # Create directory for new release
        run(f"mkdir -p /data/web_static/releases/{arch_base}")
        cmd0 = f"tar -xzf /tmp/{arch_name} -C "
        cmd = cmd0 + f"/data/web_static/releases/{arch_base}/"
        # Extract archive to the new release directory
        run(cmd)
        # Remove the uploaded archive from /tmp/
        run(f"rm /tmp/{arch_name}")
        # mv the web_static
        cmd0 = f"mv /data/web_static/releases/{arch_base}/web_static/* "
        cmd = cmd0 + f"/data/web_static/releases/{arch_base}/"
        run(cmd)
        # Delete existing symbolic link
        run(f"rm -rf /data/web_static/releases/{arch_base}/web_static")
        run(f"rm -rf /data/web_static/current")
        cmd0 = f"ln -s /data/web_static/releases/{arch_base}/ "
        cmd = cmd0 + "/data/web_static/current"
        # Create new symbolic link pointing to the new release
        run(cmd)
        return True
    except Exception as e:
        return False


def deploy():
    """Full deployment """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
