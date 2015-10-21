#!/bin/bash

for i in `seq 101 1000`; 
do     
  openssl dhparam 2048 -text >> $i; 
done
