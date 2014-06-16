# Description
This role installs and configures Oracle Instant Client on a Ubuntu Server.

# Requirements

* Ansible 1.6+
* Ubuntu 14.04+

Also, this role requires you to specify the url to download the Oracle Instant Client debs...

# Usage
Include this role in your playbooks:
```
---
- hosts: all
  roles:
    - oracle-client
...
```

# Variables 

These are the default variables. You can set any of these somewhere higher in Ansible's precedence (check 
http://docs.ansible.com/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
For example:
```
- hosts: all
  roles:
    - oracle-client
  vars:
    oracle_ic_url: http://example.com/oracle
```

## List of included variables and default values

* TODO
