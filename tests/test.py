#!/usr/bin/env python3
"""
find_module.py

A simple script to locate a Python module on your current environment.
It attempts to find the module spec and prints its location and the
current sys.path entries.
"""

import importlib.util
import sys
import argparse

def locate_module(name):
    spec = importlib.util.find_spec(name)
    if spec is None:
        print(f"Module {name!r} not found.")
    else:
        print(f"Module {name!r} found:")
        if spec.origin:
            print(f"  Origin: {spec.origin}")
        if spec.submodule_search_locations:
            for loc in spec.submodule_search_locations:
                print(f"  Location: {loc}")

def main():
    parser = argparse.ArgumentParser(description="Locate a Python module")
    parser.add_argument('module', nargs='+', help="Module name(s) to locate")
    args = parser.parse_args()

    for name in args.module:
        locate_module(name)
        print()

    print("Current sys.path:")
    for path in sys.path:
        print(f"  {path}")

if __name__ == "__main__":
    main()