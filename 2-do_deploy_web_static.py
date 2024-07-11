#!/usr/bin/python3
""" 1. Compress before sending"""
from fabric.api import env, put, run, task
import os

env.hosts = ['100.25.46.0', '54.210.60.100']

@task
def do_deploy(archive_path):
    """Deploy a compressed archive to the web servers."""
    if not os.path.exists(archive_path):
        return False
    
    try:
        arch_name = os.path.basename(archive_path)
        arch_base = os.path.splitext(arch_name)[0]
        
        # Upload archive to /tmp/ directory on remote server
        put(archive_path, "/tmp/")
        
        # Create directory for new release
        run(f"mkdir -p /data/web_static/releases/{arch_base}")
        
        # Extract archive to the new release directory
        run(f"tar -xzf /tmp/{arch_name} -C /data/web_static/releases/{arch_base}/")
        
        # Remove the uploaded archive from /tmp/
        run(f"rm /tmp/{arch_name}")
        
        # Delete existing symbolic link
        run(f"rm /data/web_static/current")
        
        # Create new symbolic link pointing to the new release
        run(f"ln -s /data/web_static/releases/{arch_base}/ /data/web_static/current")
        return True
    
    except Exception as e:
        return False
