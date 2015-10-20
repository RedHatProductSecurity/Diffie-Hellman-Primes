#!/bin/bash -vx
for BITS in "2048 4096"
do
  mkdir -p ${BITS}
  for i in `seq 1 100`;
  do
    openssl dhparam ${BITS} -text >> ${BITS}/$i
    git add .
    git commit -am "${BITS} bits, ${i}/100"
    git push
  done
done
