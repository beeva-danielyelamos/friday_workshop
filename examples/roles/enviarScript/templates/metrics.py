import psutil

cpu_percent = psutil.cpu_percent()
v_memory = psutil.virtual_memory().percent
s_memory = psutil.swap_memory().percent
d_usage = psutil.disk_usage('/').percent