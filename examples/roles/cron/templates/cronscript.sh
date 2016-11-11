#! /bin/bash

PATH_TO_SCRIPT="{{ cron_script_path }}/metrics.py"

for (( c=1; c<=6; c++ ))
do  
   ${PATH_TO_SCRIPT}
   sleep 10
done