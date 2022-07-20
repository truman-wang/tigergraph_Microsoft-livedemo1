#!/usr/bin/bash
c() {
for q in *.gsql ; do  
  gsql $q
done

gsql -g ldbc_snb install query all

for q in is6 is6r is6d is6dr ; do
./demo.py $q commentId.csv
done
}

for q in is2 is2r is2d is2dr ; do
./demo.py $q personId.csv
done
