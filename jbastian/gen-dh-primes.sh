#!/bin/bash

CPUS=$(grep -c ^processor /proc/cpuinfo)
MAX=100

[ -d 2048-2 ] || mkdir 2048-2
[ -d 2048-5 ] || mkdir 2048-5
[ -d 4096-2 ] || mkdir 4096-2
[ -d 4096-5 ] || mkdir 4096-5

for gen in 2 5 ; do
    for bits in 2048 4096 ; do
        let i=1
        while [[ $i -le $MAX ]] ; do
            let j=1
            # run one openssl process per CPU-core
            while [[ $j -le $CPUS ]] ; do
                openssl dhparam -$gen -text -out $bits-$gen/$i $bits &
                let i=i+1
                if [[ $i -gt $MAX ]] ; then break ; fi
                let j=j+1
            done
            # wait for the processes to finish before starting the next batch
            wait
            if [[ $i -gt $MAX ]] ; then break ; fi
        done
    done
done
