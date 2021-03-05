#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse

import pip_chill


def main():
    """Console script for pip_chill"""

    parser = argparse.ArgumentParser(
        description="Like `pip freeze`, but more relaxed."
    )
    parser.add_argument(
        "--no-version",
        action="store_true",
        dest="no_version",
        help="omit version numbers.",
    )
    parser.add_argument(
        "--no-chill",
        action="store_true",
        dest="no_chill",
        help="don't show installed pip-chill.",
    )
    parser.add_argument(
        "-a",
        "--all",
        "--show-all",
        action="store_true",
        dest="show_all",
        help="show all packages.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        help="list commented out dependencies too.",
    )
    parser.add_argument(
        "-c",
        "--conda",
        action="store_true",
        dest="conda",
        help="format output for conda.",
    )
    args = parser.parse_args()

    distributions, dependencies = pip_chill.chill(
        show_all=args.show_all, no_chill=args.no_chill
    )

    if args.conda:
        import os 
        import sys 
        print('name: {}'.format(os.path.split(sys.prefix)[1]))
        if "CONDA_DEFAULT_ENV" in os.environ:
            print(os.popen("conda config --show channels").read())
        else:
            print("channels:\n  - defaults")
        print("dependencies:")
        distributions = ["  - {}".format(pkg) for pkg in distributions]

    for package in distributions:
        if args.no_version:
            print(package.get_name_without_version())
        else:
            print(package)

    if args.verbose:
        for package in dependencies:
            if args.no_version:
                print(package.get_name_without_version())
            else:
                print(package)


if __name__ == "__main__":
    main()
