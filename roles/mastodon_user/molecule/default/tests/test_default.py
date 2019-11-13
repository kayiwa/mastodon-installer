import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_for_deploy_group(host):
    group = host.group("mastodon")

    assert group.exists


def test_for_deploy_user(host):
    user = host.user("mastodon")

    assert user.exists


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
