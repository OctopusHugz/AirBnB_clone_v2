#!/usr/bin/python3
from fabric.state import env

env.hosts = ['35.231.246.19', '34.227.48.93']
pack_module = __import__("1-pack_web_static")
deploy_module = __import__("2-do_deploy_web_static")


def deploy():
    """This function packs a tarball and deploys it to multiple web servers"""
    archive_path = pack_module.do_pack()
    if archive_path is None:
        return False
    deploy_status = deploy_module.do_deploy(archive_path)
    return deploy_status
