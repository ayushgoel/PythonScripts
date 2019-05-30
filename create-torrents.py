#!/usr/bin/env python3

import html
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("t", help="Magnet link")
    args = parser.parse_args()

    link = html.unescape(args.t) 
    print(link)
    res = subprocess.run(["aria2c", "-d", ".", "--bt-metadata-only=true", "--bt-save-metadata=true", "--listen-port=6881", link])
    res.check_returncode()

main()