#!/usr/bin/python3
""" 1. Compress before sending"""
from fabric import task, Connection
import os


env.hosts = ['518598-web-01', '518598-web-02']


def do_deploy(archive_path):
    """create compression file"""
    if not os.path.exists(archive_path):
        return False
    try:
        arch_name = os.path.basename(archive_path)
        arch_base = os.path.splitext(arch_name)[0]

        for h in env.hosts:
            c = Connection(h)
            # upload it to the archive 
            c.put(archive_path, "/tmp/")
            # uncompress archive
            c.run(f"tar -xzf /tmp/{arch_name} -C /data/web_static/releases/{arch_base}")
            # Delete the archive
            c.run(f"rm /tmp/{arch_name}")
            # Delete the symbolic link
            c.run(f"rm /data/web_static/current")
            # create the new symbolic link
            c.run(f"ln -s /data/web_static/releases/{arch_base} /data/web_static/current")
        return True
    except Exception as e:
        return False