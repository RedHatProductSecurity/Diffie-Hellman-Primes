#!/usr/bin/python

"""
Generates primes using openssl.
"""

import argparse
from multiprocessing.pool import Pool
from os import path
import os
import subprocess


def f(arguments):
    size, number, output_dir = arguments
    output = path.join(output_dir, '{:07d}.txt'.format(number))
    if not path.exists(output):
        subprocess.call('openssl dhparam {} -text >> {} 2> /dev/null'.format(size, output),
                        shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-w', '--workers', default=4, type=int,
                        help='Number of used workers. Best to use number of CPU cores.')
    parser.add_argument('-s', '--size', default=2048, type=int, choices=(2048, 4096),
                        help='Size of prime in bits.')
    parser.add_argument('-n', '--number', default=1000, type=int,
                        help='How many primes should be generated. They are numbered 1 ... NUMBER.'
                             'Already generated primes are skipped.')
    args = parser.parse_args()

    # Create directory if necesarry and delete not finished files
    output_dir = '{}'.format(args.size)
    if not path.exists(output_dir):
        os.mkdir(output_dir)
    for filename in os.listdir(output_dir):
        full_path = path.join(output_dir, filename)
        if path.getsize(full_path) == 0:
            os.remove(full_path)

    p = Pool(args.workers)
    arguments = []
    for i in range(1, args.number + 1):
        arguments.append([args.size, i, output_dir])

    p.map(f, arguments)
