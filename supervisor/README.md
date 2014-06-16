# Description
This role installs supervisor and sets a conf.d directory to add conf files.

# Requirements

* Ansible 1.6+
* Ubuntu 14.04+

# Usage
Include this role in your playbooks:
```
---
- hosts: all
  roles:
    - supervisor
...
```

# Variables 
These are the default variables. You can set any of these somewhere higher in ansible's precedence (check 
http://docs.ansible.com/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
For example:
```
- hosts: all
  roles:
    - supervisor
  vars:
    supervisor_config_dir: /etc/supervisor
```

## List of included variables and default values

* ```supervisor_config_dir```: Sets the default config dir. Default is ```/etc/supervisor_config_dir```
* ```supervisor_log_dir```: Sets the default log dir. Default is ```/var/log/supervisor```
* ```supervisor_log_file```: Sets the default log file. Default is ```/var/log/supervisor/supervisord.log```
* ```supervisor_pidfile```: Sets the default pid file. Default is ```/var/run/supervisord.pid```
* ```supervisor_service_name```: Sets the Upstart service name. Default is ```supervisord```
* ```supervisor_socket_file```: Sets the default socket file. Default is ```/var/run/supervisor.sock```
* ```supervisor_socket_file_mode```: Sets the default socket file mode. Default is ```0700```
