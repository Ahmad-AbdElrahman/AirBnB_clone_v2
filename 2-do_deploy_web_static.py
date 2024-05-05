#!/usr/bin/python3
from datetime import datetime
from fabric.api import put, run, env, cd
from os import path

env.hosts = ['ubuntu@54.80.218.139', 'ubuntu@54.157.155.123']

def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    d = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))


def do_deploy(archive_path):

    if path.exists(archive_path):
        archive = archive_path.split('/')[-1]
        folder = archive.split('.')[0]
        put("{}".format(archive_path), "/tmp/")
        with cd("/tmp/"):
            run("tar -xzvf {} -C /data/web_static/releases/".format(archive))
            run("mv /data/web_static/releases/web_static /data/web_static/releases/{}".format(archive, folder)) 
            run("rm -rf /tmp/{}".format(archive))
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/current /data/web_static/releases/{}".format(folder))
        return True
    return False