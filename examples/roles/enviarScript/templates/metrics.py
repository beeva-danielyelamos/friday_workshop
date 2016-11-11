#! /usr/bin/env python
import psutil
from subprocess import call

cpu_percent = psutil.cpu_percent()
v_memory = psutil.virtual_memory().percent
s_memory = psutil.swap_memory().percent
d_usage = psutil.disk_usage('/').percent

call(["echo 'cpu_percent:" + cpu_percent + "|c' | nc -u -w0 {{ ip_monitor }} {{ port_monitor }}"])
call(["echo 'v_memory:" + v_memory + "|c' | nc -u -w0 {{ ip_monitor }} {{ port_monitor }}"])
call(["echo 's_memory:" + s_memory + "|c' | nc -u -w0 {{ ip_monitor }} {{ port_monitor }}"])
call(["echo 'd_usage:" + d_usage + "|c' | nc -u -w0 {{ ip_monitor }} {{ port_monitor }}"])
