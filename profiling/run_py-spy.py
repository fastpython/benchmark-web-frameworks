# -*- coding: utf-8 -*-
"""
> What is this Py-Spy?

It's statistical profiling tool. You'll find more information in: 
https://github.com/benfred/py-spy

> How to run this script?

1. Find out what is the PID of process to profile, e.g. 'sudo ps -a'
2. Run this script 'python py-spy.py <PID> <URL>'

The <URL> is the end-point you want to profile.

"""
# Python standard library imports
import subprocess
import argparse

# 3rd party libraries
import requests

parser = argparse.ArgumentParser()
parser.add_argument("pid", help="PID for process to profile")
parser.add_argument("url", help="Tested URL, e.g. http://0.0.0.0:8000")
args = vars(parser.parse_args())

subprocess.Popen(
    [
        "sudo",
        "py-spy",
        # Sampling duration in seconds.
        "--duration",
        "10",
        # Sample rate as "samples/second" E.g. 3 sec x 2k sample/sec = 6k samples.
        "--rate",
        "500",
        # Generate flame graph called 'progile.svg'.
        "--flame",
        "profile.svg",
        # The process ID for the process we are profiling.
        "--pid",
        args["pid"],
    ]
)

result = requests.get(str(args["url"]))
