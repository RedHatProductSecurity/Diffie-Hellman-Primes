#!/bin/sh
# vim: set ts=2 sw=2 ai et:
set -e

mkdir 2048 || :
mkdir 4096 || :

for i in $(seq 251 350); do
  for size in 2048 4096; do
    echo
    echo =========================
    echo
    echo seq ${i} size ${size}
    openssl dhparam ${size} -text > ${size}/$i
  done
done
