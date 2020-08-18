#!/usr/bin/python3
from fabric.operations import local, run
from fabric.state import env

env.hosts = ['35.231.246.19', '34.227.48.93']
do_pack_module = __import__("1-pack_web_static")
do_deploy_module = __import__("2-do_deploy_web_static")
deploy_module = __import__("3-deploy_web_static")


def do_clean(number=0):
    """This function deletes out-of-date archives"""
    if number in [0, 1]:
        local("ls -1t versions | sed '1d' | xargs -I {} rm -rf versions/{}")
        cmd_1 = "ls -1t /data/web_static/releases | grep -v 'test' "
        cmd_2 = "| sed '1d' | xargs -I {} rm -rf /data/web_static/releases/{}"
        cmd_string = cmd_1 + cmd_2
        run(cmd_string)
    else:
        ending = "| sed '1," + number + "d' | xargs -I {} rm -rf versions/{}"
        ending2 = "| grep -v 'test' | sed '1," +\
            number + "d' | xargs -I {} rm -rf /data/web_static/releases/{}"
        v_cmd_string = "ls -1t versions " + ending
        local(v_cmd_string)
        r_cmd_string = "ls -1t /data/web_static/releases " + ending2
        run(r_cmd_string)
