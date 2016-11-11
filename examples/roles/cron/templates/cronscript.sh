#! /bin/bash

PATH_TO_SCRIPT= {{ cron_script_path }}/{cron_script_name}

for (( c=1; c<=6; c++ ))
do  
   ./${PATH_TO_SCRIPT}
   wait(10)
done