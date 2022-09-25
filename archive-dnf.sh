#!/bin/bash

# backing-up /tmp/dnf file, if exists replace with newer verion and store the older with .old backup file

if test -f /tmp/archive.tar.gz; then
	mv /tmp/archive.tar.gz /tmp/archive.tar.gz.OLD
	tar acf /tmp/archive.tar.gz /etc/dnf/
else
	tar acf /tmp/archive.tar.gz /etc/dnf/
fi