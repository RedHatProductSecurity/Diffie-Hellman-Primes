#!/usr/bin/python

# generate 100 prime numbers (Diffie-Hellman Parameters) using both
# the 2 and 5 generators with 2048-bits and 4096-bits
# for https://github.com/RedHatProductSecurity/Diffie-Hellman-Primes
# Jeff Bastian <jbastian@redhat.com>, 2015-10-20

from multiprocessing import Pool
from os import mkdir
from os.path import isdir
from subprocess import call

def dh(t):
    output = t[0]
    bits = t[1]
    gen = t[2]
    cmd = "openssl dhparam -%d -text -out %d-%d/%d %d" % (gen,
        bits, gen, output, bits)
    call(cmd, shell=True)

if __name__ == '__main__':
    for d in "2048-2", "2048-5", "4096-2", "4096-5":
        if not isdir(d):
            mkdir(d)

    p = Pool()
    count = range(1, 101) + range(1, 101) + range(1, 101) + range(1, 101)
    bits = [2048] * 200 + [4096] * 200
    gen = [2] * 100 + [5] * 100 + [2] * 100 + [5] * 100
    x = zip(count, bits, gen)
    p.map(dh, x)
