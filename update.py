from git import *
import time
from datetime import datetime, date
import os, subprocess
start = time.time()
## WARNING ##
# This script should not be changed without caution. 
# It will auto-deploy 4 times a day and changes can break the auto-deploy infrastructure.
## WARNING ##
repo = Git('/var/pip')
out = repo.pull('origin', 'master')
if out == 'Already up to date.' or out == 'Already up-to-date.':
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print('[{0} - {1}] Found nothing to update in {2}s'.format(today,current_time,str(time.time()-start)[:3]))
else:
    pipout = os.system("pip3 install -U -r /var/pip/requirements.txt")
    print(pipout)
