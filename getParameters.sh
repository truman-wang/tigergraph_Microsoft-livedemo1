rm commentId.csv personId.csv
root=/home/tigergraph/sf*/initial_snapshot/dynamic
n1=`ls ${root}/Comment/*.csv | wc -l`
n2=`ls ${root}/Person/*.csv | wc -l`

for f in $root/Comment/*.csv; do 
  head -$((100000/n1+1)) $f \
      | awk 'BEGIN { FS = "|" } ; NR!=1 { print $2 }' >> commentId.csv
done
wc -l commentId.csv

for f in $root/Person/*.csv; do
  head -$((100000/n2+1)) $f \
      | awk 'BEGIN { FS = "|" } ; NR!=1 { print $2 }' >> personId.csv
done
wc -l personId.csv