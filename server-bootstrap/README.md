# Description
This role sets some sane defaults on a freshly installed Ubuntu Server. It can
also install some pyth

# Requirements

* Ansible 1.6+
* Ubuntu 14.04+

# Usage
Include this role in your playbooks:
```
---
- hosts: all
  roles:
    - server-bootstrap
...
```

# Variables 
These are the default variables. You can set any of these somewhere higher in ansible's precedence (check 
http://docs.ansible.com/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
For example:
```
- hosts: all
  roles:
    - server-bootstrap
  vars:
    bootstrap_upgrade_system: true
```

## List of included variables and default values

### General
* ```bootstrap_install_dev_packages```: Installs some useful packages for development. Default is ```false```
* ```bootstrap_local_sources```: Replaces the default ubuntu repos with a local mirror. Default is ```false```
* ```bootstrap_locale```: Sets the default locale. Default is ```en_US.UTF-8```
* ```bootstrap_log_dir```: Sets a specific log_dir Default is ```/var/log```
* ```bootrstrap_timezone```: Sets the server timezone. Default is ```America/Argentina/Buenos_Aires```
* ```bootstrap_upgrade_system```: Performs a dist-upgrade. Default is ```false```

### Python install
* ```bootstrap_python_install```: Installs some packages for python development. Default is ```true```
* ```bootstrap_virtualenv_workon_home```: Virtualenv home directory. Default is ```Envs```

### Security
* ```bootstrap_ufw_state```: Enable ufw. Default is ```disabled```
* ```bootstrap_ufw_allowed_ports```: Enable ports via ufw. It's a yaml list. Default is ```80```
* ```bootstrap_ubuntu_unattended_upgrades```: Enable ubuntu unattended upgrades. Default is ```true```
