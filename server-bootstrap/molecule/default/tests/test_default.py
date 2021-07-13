import os
import testinfra
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    "build-essential",
    "bzip2",
    "curl",
    "libssl-dev",
    "locales",
    "ntp",
    "openssl",
    "software-properties-common",
    "ssl-cert",
    "wget",
])
def test_paquetes_esenciales(host, name):
    p = host.package(name)
    assert p.is_installed


@pytest.mark.parametrize('name', [
    "bash",
    "git",
    "htop",
    "silversearcher-ag",
    "vim",
    "tree",
    "multitail",
    "most",
    "unzip",
])
def test_paquetes_desarrollo(host, name):
    p = host.package(name)
    assert p.is_installed
