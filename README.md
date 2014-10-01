# Ansible roles [![Build Status](https://travis-ci.org/MSA-Argentina/ansible-roles.svg?branch=master)](https://travis-ci.org/MSA-Argentina/ansible-roles)

Some useful roles to speed up deployments with Ansible.

## How to use
* Clone this repo
* Modify `ansible.cfg` (usually `/etc/ansible/ansible.cfg`) and include this line:
```
roles_path = /path/to/cloned_repo
```
* Finally, use any of these roles in your playbooks:
```
---
- hosts: all
  roles:
    - server-bootstrap
    - postgresql
    - nginx
...
```

# Credits

* Monit role from https://github.com/ansibles/monit
* PostgreSQL role from https://github.com/ansibles/postgresql
* Memcached role from https://github.com/bennojoy/memcached
* ElasticSearch role from https://github.com/deimosfr/ansible-elasticsearch
* Java role from https://github.com/vrischmann/ansible-role-java
