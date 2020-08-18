#!/usr/bin/python3
from fabric.operations import local, run
from fabric.state import env

env.hosts = ['35.231.246.19', '34.227.48.93']


def do_clean(number=0):
    """This function deletes out-of-date archives"""
    if number in [0, 1]:
        local("ls -ltr versions | awk 'NR > 1' | xargs rm -rf")
        run("""ls -ltr /data/web_static/releases | awk 'NR > 1'
         | grep -v 'test' | xargs rm -rf""")
    else:
        v_cmd_string = "ls -ltr versions | awk 'NR > "\
            + number + "' | xargs rm -rf"
        local(v_cmd_string)
        r_cmd_string = "ls -ltr /data/web_static/releases | awk 'NR > "\
            + number + "' | grep -v 'test' | xargs rm -rf"
        run(r_cmd_string)
