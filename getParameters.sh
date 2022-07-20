head -10001 /home/tigergraph/sf1000/initial_snapshot/dynamic/Comment/part-00000-4afce684-82c0-4234-b6f6-aa2c132c2627-c000.csv | awk 'BEGIN { FS = "|" } ; NR!=1 { print $2 }' > commentId.csv
wc -l commentId.csv
head -10001 /home/tigergraph/sf1000/initial_snapshot/dynamic/Person/part-00000-aece135f-b6fb-4f79-8f48-ddb14530c224-c000.csv | awk 'BEGIN { FS = "|" } ; NR!=1 { print $2 }' > personId.csv
wc -l personId.csv