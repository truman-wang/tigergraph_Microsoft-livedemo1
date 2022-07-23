# TigerGraph demo on a cluster
Slide
https://docs.google.com/presentation/d/19mgHglhpRXOaefibprstugfNKlGuwbp_6b9TLS6sCN4/edit?usp=sharing

## Introduction
TigerGraph has two modes:
1. Non-distributed mode: the data is gethered at the local node. This mode targets for transaction workload (low latency for small query). 
2. Distributed mode: query is executed on all the nodes in parallel. This mode targets for analytical workload (large query that touch a large amount of data).

## Data schema and statistics
![alt text](./schema.png)
1T data: ~2.4 B vertices and ~17 B edges
| Comment  | Post | Person | Forum |
|-------|-------|-------|-------|
|1,876,785,283| 519,738,978 |  3,399,580 | 33,168,124 |

10T data: ~24 B vertices and ~173 B edges
| Comment  | Post | Person | Forum |
|-------|-------|-------|-------| 
|18,880,439,325| 4,461,342,990 |  26,384,952 | 257,338,738 |

## Results
### 1T LDBC SNB data
#### Environment
- 4x GCP n2d-highmem-64 
- Each machine has 64vCPU/512G RAM
- TigerGraph 3.7.0-RC

#### Latency (in millisecond)
IS2 persontiles: 
|CNT    |THEAD  |P50    |P90    |P95    |P99    |AVG    |QPS    |
|-------|-------|-------|-------|-------|-------|-------|-------|
|16000  |32     |42     |58     |63     |77     |44     |1128   |

IS6 persontiles: 
|CNT    |THEAD  |P50    |P90    |P95    |P99    |AVG    |QPS    |
|-------|-------|-------|-------|-------|-------|-------|-------|
|16000  |32     |30     |47     |50     |66     |33     |1485   |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|12000 |24 |35 |45 |49 |60 |36 |786 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|12000 |24 |24 |31 |35 |46 |25 |1136 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|8000 |16 |33 |43 |47 |58 |34 |458 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|8000 |16 |22 |27 |28 |38 |22 |699 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|4000 |8 |32 |42 |45 |56 |33 |236 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|4000 |8 |22 |25 |26 |40 |22 |356 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|2000 |4 |31 |39 |41 |51 |32 |125 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|2000 |4 |22 |25 |26 |34 |22 |176 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|500 |1 |32 |39 |42 |48 |33 |30 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|500 |1 |23 |26 |28 |31 |24 |42 |




### 3T LDBC SNB data
#### Environment 
- 10x GCP n2d-highmem-64 
- Each machine has 64vCPU/512G RAM
- TigerGraph 3.7.0-RC

#### Latency (in millisecond)

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|16000 |32 |64 |78 |84 |113 |66 |758 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|16000 |32 |53 |65 |70 |99 |54 |914 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|8000 |16 |63 |76 |81 |101 |64 |244 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|8000 |16 |53 |62 |66 |85 |54 |292 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|4000 |8 |63 |74 |79 |92 |63 |124 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|4000 |8 |54 |63 |67 |79 |55 |144 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|2000 |4 |63 |74 |79 |93 |63 |62 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|2000 |4 |54 |63 |66 |78 |54 |73 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|500 |1 |67 |78 |83 |93 |67 |15 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|500 |1 |59 |69 |72 |83 |59 |17 |






### 10T LDBC SNB data
#### Environment 
- 20x GCP n2d-highmem-96 
- Each machine has 96vCPU/768G RAM
- TigerGraph 3.7.0-RC

#### Latency (in millisecond)

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|16000 |32 |151 |283 |337 |414 |185 |264 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|16000 |32 |132 |281 |351 |428 |156 |313 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|8000 |16 |159 |322 |345 |390 |205 |76 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|8000 |16 |134 |216 |303 |359 |150 |103 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|4000 |8 |183 |313 |329 |363 |219 |36 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|4000 |8 |144 |171 |277 |320 |154 |51 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|2000 |4 |181 |326 |342 |372 |227 |17 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|2000 |4 |163 |186 |246 |341 |168 |23 |

IS2 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|500 |1 |187 |325 |336 |367 |234 |4 |

IS6 persontiles:
|CNT |THEAD |P50 |P90 |P95 |P99 |AVG |QPS |
|-------|-------|-------|-------|-------|-------|-------|-------|
|500 |1 |165 |189 |240 |343 |173 |6 |