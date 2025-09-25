#!/usr/bin/env python3
'''Lab 3 Inv 2 free_space function'''
# Author ID: [seneca_id]

import subprocess

def free_space():
    p = subprocess.Popen(
        "df -h / | tail -1 | awk '{print $4}'",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    output = p.communicate()
    return output[0].decode("utf-8").strip()

if __name__ == "__main__":
    print(free_space())
