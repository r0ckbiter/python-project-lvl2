#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', metavar='FORMAT', help='set format of output')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
