#!/bin/bash
# Tests the syntax of a playbook
echo "################################"
echo "Testing playbook syntax"
echo "Versions:"
echo "Ansible Version: $(ansible --version)"
echo "Ansible Playbook Version: $(ansible-playbook --version)"
echo "Vagrant Version: $(vagrant --version)"
echo "################################"

echo localhost > inventory
ansible-playbook --syntax-check --list-tasks -i inventory $1
rm inventory

exit 0
