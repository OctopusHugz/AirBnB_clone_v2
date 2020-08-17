#!/usr/bin/python3
from os import path
from fabric.decorators import hosts
from fabric.operations import put, run


@hosts(['35.231.246.19', '34.227.48.93'])
def do_deploy(archive_path):
    """This function distributes an archive to web servers"""
    try:
        if not path.exists(archive_path):
            return False
        archive_name = archive_path[9:]
        dest_path = "/tmp/" + archive_name
        filename = archive_name[:-4] + "/"
        release_path = "/data/web_static/releases/"
        frp = release_path + filename
        put(archive_path, dest_path)
        cmd_string = "mkdir -p " + frp
        run(cmd_string)
        cmd_string2 = "tar -xzf " + dest_path + " -C " + frp
        run(cmd_string2)
        cmd_string3 = "rm " + dest_path
        run(cmd_string3)
        cmd_string4 = "mv " + frp + "web_static/* " + frp
        run(cmd_string4)
        cmd_string5 = "rm -rf " + frp + "web_static"
        run(cmd_string5)
        cmd_string6 = "rm -rf /data/web_static/current"
        run(cmd_string6)
        cmd_string7 = "ln -s " + frp + " /data/web_static/current"
        run(cmd_string7)
        return True
    except:
        return False
