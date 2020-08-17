#!/usr/bin/python3
from datetime import datetime
from os import path, makedirs
from fabric.api import local


def do_pack():
    """This function packs the contents of the web_static folder into a tgz
    archive"""
    try:
        now = datetime.now()
        now_date = str(now.year) + str(now.month) + str(now.day) + str(now.hour)\
            + str(now.minute) + str(now.second) + ".tgz"
        archive_name = "web_static_" + now_date
        if not path.exists("versions/"):
            makedirs("versions/")
        cmd_string = "tar -cvzf versions/" + archive_name + " web_static"
        local(cmd_string)
        return "versions/" + archive_name
    except:
        return None
