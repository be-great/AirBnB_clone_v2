#!/usr/bin/python3
""" 1. Compress before sending"""
from datetime import datetime
from fabric.api import local
import os


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
