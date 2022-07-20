#!/usr/bin/python3
import requests
import time
import numpy as np
from random import randrange
import sys


q = sys.argv[1]
ids = open(sys.argv[2]).readlines()
N = 500
times = []
for i in range(N):
  vid = ids[randrange(len(ids))].strip()
  t0 = time.time()
  response = requests.get(f'http://127.0.0.1:9000/query/ldbc_snb/{q}', params={"id":vid}).json()
  times.append((time.time() - t0)*1000)

  if (i+1) % 100 == 0:
    print(i+1, response)

percentiles = np.percentile(times, [50, 90, 95, 99])
print()
print(f'{q.upper()} persontiles: ')
print('|' + '\t|'.join(['CNT', 'P50','P90','P95','P99']) + '\t|')
print('|' + '|'.join(['-------']*5) + '|')
print(f'|{N}\t|' + '\t|'.join([f'{p:.2f}' for p in percentiles]) + '\t|')
