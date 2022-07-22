#!/usr/bin/bash
for q in *.gsql ; do  
  gsql $q
done

gsql -g ldbc_snb install query all


for q in is2; do
./demo.py $q personId.csv
done

for q in is6; do
./demo.py $q commentId.csv
done