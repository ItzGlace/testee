#!/usr/bin/env python3
import os
import time
import requests
import subprocess as sp

os.system("x-ui status > test.txt")

def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            os.system("x-ui restart")
        else:
            print('string does not exist in a file')

status = search_str('/root/test.txt', 'Result: exit-code')
time.sleep(5)
status = search_str('/root/test.txt', 'Result: exit-code')
time.sleep(5)
status = search_str('/root/test.txt', 'Result: exit-code')
time.sleep(5)
status = search_str('/root/test.txt', 'Result: exit-code')
time.sleep(5)
status = search_str('/root/test.txt', 'Result: exit-code')
time.sleep(5)
status = search_str('/root/test.txt', 'Result: exit-code')
time.sleep(5)
status = search_str('/root/test.txt', 'Result: exit-code')
time.sleep(5)
status = search_str('/root/test.txt', 'Result: exit-code')
time.sleep(5)
status = search_str('/root/test.txt', 'Result: exit-code')
time.sleep(5)
status = search_str('/root/test.txt', 'Result: exit-code')
time.sleep(5)
