#!/bin/bash -vx
SEQ="2048 4096"
for BITS in $SEQ
do
  mkdir -p ${BITS}
  for i in `seq 1 100`;
  do
    openssl dhparam ${BITS} -text >> ${BITS}/${i}
    git add .
    git commit -am "${BITS}/${i}"
    git push
  done
done
