#!/usr/bin/python3

import argparse
import sys

import sorter

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int, help="Max number of files in each directory")
parser.add_argument("-r", "--reverse",
                    help="Takes the files in the directories in the working dir, and move them to working dir",
                    action="store_true")


def main():
    args = parser.parse_args()
    if args.number:
        sorter.create_dirs(sorter.separate_by_number(args.number))
    elif args.reverse:
        sorter.join_from_dirs()
    else:
        print("Error: You must select an option")
        print("Use buckets --help to see the options available")
        sys.exit(1)


if __name__ == "__main__":
    main()
