DH primes
=========

* `2048/` contains 2048-bit primes.
* `4096/` contains 4096-bit primes.


Primes 1-130
------------

These primes (both 2048 and 4096) were generated with
`OpenSSL 1.0.1k-fips 8 Jan 2015` on a Fedora 21 container
running on a CoreOS virtual machine in AWS.

See the `generate.sh` script.
It uses the default 2 generator.


Primes 131-250
--------------

These primes (both 2048 and 4096) were generated with
`OpenSSL 1.0.2d 9 Jul 2015 (Library: OpenSSL 1.0.2b 11 Jun 2015)` on an Alpine 3.2 container
running on a CoreOS virtual machine in AWS.

See the Dockerfile and `generate.sh` script.
It uses the default 2 generator.


Primes 251-450
--------------

These primes (both 2048 and 4096) were generated with
`OpenSSL 1.0.2d 9 Jul 2015 (Library: OpenSSL 1.0.2b 11 Jun 2015)` on an Alpine 3.2 container
running on a CoreOS virtual machine in Digital Ocean.

See the Dockerfile and `generate.sh` script.
It uses the default 2 generator.
