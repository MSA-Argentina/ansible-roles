# Description
This role installs apache2 on Ubuntu 14.04 using the official repos.
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
    - apache
...
```

# Variables 
These are the default variables. You can set any of these somewhere higher in ansible's precedence (check 
http://docs.ansible.com/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
For example:
```
- hosts: all
  roles:
    - apache
  vars:
    apache_install_mod-wsgi: false
```

## List of included variables and default values

* ```apache_mpm```: Enable the specified mpm module. Default is ```prefork```. Other options are ```event``` and ```worker```.
* ```apache_install_mod-wsgi```: Installs mod-wsgi. Default is ```yes```
* ```apache_modules```: A list of modules to enable. Defaults: ```rewrite```, ```ssl``` and ```wsgi```

# Handlers included

* restart apache
