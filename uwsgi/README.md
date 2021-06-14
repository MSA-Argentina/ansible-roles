# Description
This role installs uwsgi in emperor mode and sets an apps directory to add application ini files.

# Requirements

* Ansible 1.6+
* Ubuntu 14.04+

# Usage
Include this role in your playbooks:
```
---
- hosts: all
  roles:
    - uwsgi
...
```

# Variables 
These are the default variables. You can set any of these somewhere higher in ansible's precedence (check 
http://docs.ansible.com/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
For example:
```
- hosts: all
  roles:
    - uwsgi
  vars:
    uwsgi_service_name: uwsgi
```

## List of included variables and default values

* ```uwsgi_apps_available_dir```: Sets the apps_available dir, where you put your application specific config files. Default is ```/etc/uwsgi/apps_available```
* ```uwsgi_apps_enabled_dir```: Sets the apps_enabled dir, where you symlink your available apps. Default is ```/etc/uwsgi/apps_enabled```
* ```uwsgi_config_directory```: Sets the base config dir. Default is ```/etc/uwsgi```
* ```uwsgi_log_directory```: Sets the default log directory. Default is ```/var/log/uwsgi```
* ```uwsgi_service_name```: Sets the Upstart service name. Default is ```uwsgi```
* ```uwsgi_systemd```: If true use systemd, create service {{uwsgi_service_name}}.service . Default is ```false```
* ```uwsgi_systemd_after```: Services After systemd option, str with space sep. Default is ```"syslog.target"``` 
* ```uwsgi_systemd_requires```: Services Requires sysmted option, str with space sep. Default is None, not add this option if not explicit override.
