#!/usr/bin/env python3
import os
import time
import pexpect
import sys
import datetime

now = datetime.datetime.now()
now = str(now)
now = now.replace(" ", "*")
now = now.replace(".", "*")
Name = f'{now}==RU01'
now = datetime.datetime.now()

os.system(f"cp /etc/x-ui-english/x-ui-english.db /etc/x-ui-english/{Name}.db")

child = pexpect.spawn(f"rsync /etc/x-ui-english/{Name}.db root@198.244.147.34:/root/Backups")
child.expect("root@198.244.147.34's password:")
child.sendline("@Glace702As")
child.expect("#")
