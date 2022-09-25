#!/bin/bash

# log the date and time the script was last executed

date >> /tmp/script.log

cat /proc/version >> /tmp/script.log


echo "#***************************#" >> /tmp/script.log
