# Description
This role installs the last version redis-server on Ubuntu 14.04 using a ppa.

# Requirements

* Ansible 1.6+
* Ubuntu 14.04+

# Usage
Include this role in your playbooks:
```
---
- hosts: all
  roles:
    - redis
...
```

# Variables 

These are the default variables. You can set any of these somewhere higher in Ansible's precedence (check 
http://docs.ansible.com/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
For example:
```
- hosts: all
  roles:
    - redis
  vars:
    redis_ppa: ppa:chris-lea/redis-server
```

## List of included variables and default values

* ```redis_ppa```: PPA for redis. Default is ```ppa:chris-lea/redis-server```

# Handlers included

* restart redis
