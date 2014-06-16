#!/bin/bash

if [ "$UID" -ne 0 ]; then
    echo "This script must be run as root"
    exit 1
fi

# Renaming archive.ubuntu.com, even if it's prepended by a country code (ie. ar.archive.ubuntu.com) and doing a backup
# excluiding the backports and proposed words, which in this case we don't mirror
sed -i.original '/backports\|proposed/! s/^deb http:\/\/.*archive.ubuntu.com/deb http:\/\/manic.msa/g' /etc/apt/sources.list

# Renaming security.ubuntu.com
sed -i 's/^deb http:\/\/security.ubuntu.com/deb http:\/\/manic.msa/g' /etc/apt/sources.list
