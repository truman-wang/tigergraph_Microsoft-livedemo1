#!/usr/bin/python3
import requests
import time
import numpy as np
from random import randrange
import sys
from multiprocessing import Pool, current_process
from random import shuffle
import os
from glob import glob
q = sys.argv[1]
thread = int(sys.argv[2])

if q == 'is2':
  param = 'personId.csv'
elif q == 'is6':
  param = 'commentId.csv'
else:
  exit

ids = open(param).readlines()
N = 1000*thread
vid = [int(id.strip()) for id in ids]
shuffle(vid)
vid = vid[:N]

# print an example results
# response = requests.get(f'http://127.0.0.1:9000/query/ldbc_snb/{q}', params={"id":vid[0]}).json()
# print(response)

for fn in glob('ForkPool*.csv'):
  try:
    os.remove(fn)
  except OSError:
    pass

def test(vid):
  t0 = time.time()
  n = current_process().name
  response = requests.get(f'http://127.0.0.1:9000/query/ldbc_snb/{q}', params={"id":vid}).json()
  with open(f'{n}.csv', 'a') as f:
    f.write(str(response)+'\n')
  return (time.time() - t0)*1000
  

t0 = time.time()
with Pool(processes=thread) as pool:
  times = pool.map(test, vid)
tot_time = time.time() - t0
times = np.array(times)
percentiles = np.percentile(times, [50, 90, 95, 99]).tolist()
results = [N, thread] + percentiles + [np.average(times), N/tot_time]


print()
print(f'{q.upper()} persontiles: ')
print('|' + '\t|'.join(['CNT', 'THEAD', 'P50','P90','P95','P99','AVG','QPS']) + '\t|')
print('|' + '|'.join(['-------']*8) + '|')
print('|' + '\t|'.join([f'{p:.0f}' for p in results]) + '\t|')
