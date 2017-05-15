# Description
This role installs psql (PostgreSQL client) only.

# Requirements

* Ansible 1.6+
* Ubuntu 14.04+

# Usage
Include this role in your playbooks:
```
---
- hosts: all
  roles:
    - postgresql-client
...
```
