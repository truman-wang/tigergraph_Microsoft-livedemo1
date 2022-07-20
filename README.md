# TigerGraph demo on a cluster
## Results
### 1T LDBC SNB data
environment: 4x 
time is presented in millisecond

IS6 persontiles: 
|CNT    |P50    |P90    |P95    |P99    |
|-------|-------|-------|-------|-------|
|500    |28.89  |32.54  |34.02  |42.59  |

IS6 with EDGE* persontiles: 
|CNT    |P50    |P90    |P95    |P99    |
|-------|-------|-------|-------|-------|
|500    |209.66 |220.83 |224.14 |239.86 |

IS6 distributed persontiles: 
|CNT    |P50    |P90    |P95    |P99    |
|-------|-------|-------|-------|-------|
|500    |657.31 |666.47 |856.46 |858.67 |

IS6 distributed with EDGE* persontiles: 
|CNT    |P50    |P90    |P95    |P99    |
|-------|-------|-------|-------|-------|
|500    |1101.86        |1318.10        |1516.24        |1725.84        |

IS2 persontiles: 
|CNT    |P50    |P90    |P95    |P99    |
|-------|-------|-------|-------|-------|
|500    |41.18  |51.47  |55.61  |63.58  |