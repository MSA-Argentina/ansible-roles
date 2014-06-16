# Description
This role installs nginx on Ubuntu 14.04 using the official ppa. It includes an optimized
conf.

# Requirements

* Ansible 1.6+
* Ubuntu 14.04+

# Usage
Include this role in your playbooks:
```
---
- hosts: all
  roles:
    - nginx
...
```

# Variables 

These are the default variables. You can set any of these somewhere higher in Ansible's precedence (check 
http://docs.ansible.com/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
For example:
```
- hosts: all
  roles:
    - nginx
  vars:
    nginx_user: nginx
```

## List of included variables and default values

* ```nginx_access_log```: Location of nginx access log. Default is ```/var/log/nginx/access.log```
* ```nginx_error_log```: Location of nginx error log. Default is ```/var/log/nginx/error.log```
* ```nginx_enable_monit```: Enable monitoring with monit. Default is ```false```
* ```nginx_install_from_ppa```: If true, install nginx for the official ppa. If false, it uses the official ubuntu repos. error log. Default is ```true```
* ```nginx_pid_file```: Location of nginx pid file. Default is ```/var/run/nginx.pid```
* ```nginx_ppa```: Defines the ppa address Default is ```ppa:nginx/stable```
* ```nginx_user```: Defines the nginx default user. Default is ```www-data```
* ```nginx_worker_connections```: Defines the nginx max worker connections user. Default is ```768```
* ```nginx_worker_processes```: Defines the nginx worker processes. Default is ```2```

# Handlers included

* restart nginx
