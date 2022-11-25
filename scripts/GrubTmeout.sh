#!/bin/bash

# checking grep timeout settings forfrom "/etc/defualt/grub" configuration file

if grep -q '5' /etc/default/grub;then
	echo "Grub has timeout of 5 seconds."
else
	echo "Grub does not have a timeout of 5 seconds."
fi
