#!/usr/bin/python3
""" 1. Compress before sending"""
from fabric.api import local, env, put, run
import os


env.hosts = ['518598-web-01', '518598-web-02']


def do_deploy(archive_path):
    """create compression file"""
    if not os.path.exists(archive_path):
        return False
    try:
        arch_name = os.path.basename(archive_path)
        arch_base = os.path.splitext(arch_name)[0]
        # upload it to the archive
        put(archive_path, "/tmp/")
        # uncompress archive
        cmd0 = f"tar -xzf /tmp/{arch_name} -C "
        cmd = cmd0 + "/data/web_static/releases/{arch_base}"
        run(cmd)
        # Delete the archive
        run(f"rm /tmp/{arch_name}")
        # Delete the symbolic link
        run(f"rm /data/web_static/current")
        # create the new symbolic link
        cmd0 = f"ln -s /data/web_static/releases/{arch_base} "
        cmd = cmd0 + "/data/web_static/current"
        run(cmd)
        return True
    except Exception as e:
        return False
