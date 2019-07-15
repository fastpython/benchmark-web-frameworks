# -*- coding: utf-8 -*-
"""
> What is this wrk?

It's HTTP benchmarking tool. You'll find more information in:
https://github.com/wg/wrk

> How to use this script?

Pass the tested end-point for the script. E.g. 'python run_wrk.py
http://0.0.0.0:8000'. Script doesn't do anything special, but just stores
what parameters are used and helps you to remember how wrk should be used.

Example wrk command:
wrk -d 20 -c 1 -t 1 --timeout 60 http://0.0.0.0:8000

"""
# Python standard library imports
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Tested URL, e.g. http://0.0.0.0:8000")
args = vars(parser.parse_args())

subprocess.run(
    [
        "wrk",
        # Duration of the test, e.g. 2s, 2m, 2h
        "-d",
        "60",
        # Total number of HTTP connections to keep open with each thread
        # handling  N = connections/threads
        "-c",
        "1",
        # Total number of threads to use
        "-t",
        "1",
        # Record a timeout if a response is not received within this amount
        # of time.
        "--timeout",
        "60",
        str(args["url"]),
    ]
)
