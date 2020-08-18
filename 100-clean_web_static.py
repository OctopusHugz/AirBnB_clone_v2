#!/usr/bin/python3
from fabric.operations import run
from fabric.state import env

env.hosts = ['35.231.246.19', '34.227.48.93']
pack_module = __import__("1-pack_web_static")
deploy_module = __import__("2-do_deploy_web_static")


def do_clean(number=0):
    """This function deletes out-of-date archives"""
    if number in [0, 1]:
        run("ls -1t | awk 'NR > 1' | xargs rm")
    else:
        cmd_string = "ls -1t | awk 'NR > " + number + "' | xargs rm"
        run(cmd_string)
