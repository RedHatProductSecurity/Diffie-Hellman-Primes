#!/bin/bash

mkdir 2048

for i in `seq 1 100`;
do
    echo "(Loop $i)"
    openssl dhparam 2048 -text >> 2048/$i
done

times
