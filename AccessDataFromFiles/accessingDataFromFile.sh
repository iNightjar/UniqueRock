#!/bin/bash
#author: iNightjar

grep -i 'error' messages > error-output
grep -i 'warn' messages > warn-output
grep -i 'fail' messages > fail-output

# grep -i 'fail' messages