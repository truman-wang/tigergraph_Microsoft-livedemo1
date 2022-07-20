#!/usr/bin/bash
for q in *.gsql ; do  
  gsql $q
done

gsql -g ldbc_snb install query all

for q in is6 is6r is6d ; do
./demo.py $q commentId.csv
done

for q in is2 is2r is2d ; do
./demo.py $q personId.csv
done
