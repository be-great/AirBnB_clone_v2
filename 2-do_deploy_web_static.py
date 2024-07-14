#!/usr/bin/python3
""" 1. Compress before sending """
from fabric.api import env, put, run
import os


env.hosts = ['34.232.76.39', '52.91.132.184']


def do_deploy(archive_path):
    """ Deploy a compressed archive to the web servers. """
    if not os.path.exists(archive_path):
        return False
    arch_name = archive_path.split('/')[-1]
    arch_base0 = '/data/web_static/releases/'
    arch_base = arch_base0 + "{}".format(arch_name.split('.')[0])
    tmp = "/tmp/" + arch_name

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(arch_base))
        run("tar -xzf {} -C {}/".format(tmp, arch_base))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(arch_base, arch_base))
        run("rm -rf {}/web_static".format(arch_base))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(arch_base))
        return True
    except Exception as e:
        return False
