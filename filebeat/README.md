# Description
This role installs FileBeat on Ubuntu 16.04 using the official APT repository.

# Requirements

* Ansible 1.6+
* Ubuntu 14.04+

# Usage
Include this role in your playbooks:
```
---
- hosts: all
  roles:
    - filebeat
...
```
