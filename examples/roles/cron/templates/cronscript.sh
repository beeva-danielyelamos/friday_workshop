#! /bin/bash

PATH_TO_SCRIPT={{ script_path }}

for (( c=1; c<=6; c++ ))
do  
   ./${PATH_TO_SCRIPT}
   wait(10)
done