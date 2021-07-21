import os
import testinfra
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    "libsqlite3-dev",
    "python-apt-common",
    #"python-dev",
    "python3-dev",
    "python3-pip",
    "software-properties-common",
    "virtualenv",
    "python3-setuptools",
    "sqlite3",
])
def test_paquetes_python(host, name):
    p = host.package(name)

    assert p.is_installed


# @pytest.mark.parametrize('package', [])
# def test_pip(host, package):
    # p = host.pip_package.get_packages(pip_path='pip3.6')
    # assert package in p
