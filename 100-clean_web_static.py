#!/usr/bin/python3
from fabric.operations import local, run
from fabric.state import env

env.hosts = ['35.231.246.19', '34.227.48.93']


def do_clean(number=0):
    """This function deletes out-of-date archives"""
    if number in [0, 1]:
        local("ls -1t versions | awk 'NR > 1' | xargs rm")
        run("ls -1t /data/web_static/releases | awk 'NR > 1' | xargs rm")
    else:
        v_cmd_string = "ls -1t versions | awk 'NR > " + number + "' | xargs rm"
        local(v_cmd_string)
        r_cmd_string = "ls -1t /data/web_static/releases | awk 'NR > "\
            + number + "' | xargs rm"
        run(r_cmd_string)
