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

#### IS6 Latency (in millisecond) 
|CNT    |THEAD  |P50    |P90    |P95    |P99    |AVG    |QPS    |
|-------|-------|-------|-------|-------|-------|-------|-------|
|28000  |28     |35     |56     |60     |72     |39     |700    |

|CNT    |THEAD  |P50    |P90    |P95    |P99    |AVG    |QPS    |
|-------|-------|-------|-------|-------|-------|-------|-------|
|24000  |24     |32     |48     |52     |59     |35     |673    |

|CNT    |THEAD  |P50    |P90    |P95    |P99    |AVG    |QPS    |
|-------|-------|-------|-------|-------|-------|-------|-------|
|16000  |16     |27     |31     |33     |45     |27     |590    |

|CNT    |THEAD  |P50    |P90    |P95    |P99    |AVG    |QPS    |
|-------|-------|-------|-------|-------|-------|-------|-------|
|8000   |8      |26     |30     |31     |44     |27     |296    |

#### IS2 Latency (in millisecond) 
|CNT    |THEAD  |P50    |P90    |P95    |P99    |AVG    |QPS    |
|-------|-------|-------|-------|-------|-------|-------|-------|
|28000  |28     |47     |65     |71     |88     |49     |563    |

|CNT    |THEAD  |P50    |P90    |P95    |P99    |AVG    |QPS    |
|-------|-------|-------|-------|-------|-------|-------|-------|
|24000  |24     |43     |57     |62     |79     |45     |529    |

|CNT    |THEAD  |P50    |P90    |P95    |P99    |AVG    |QPS    |
|-------|-------|-------|-------|-------|-------|-------|-------|
|16000  |16     |39     |50     |55     |70     |40     |391    |

|CNT    |THEAD  |P50    |P90    |P95    |P99    |AVG    |QPS    |
|-------|-------|-------|-------|-------|-------|-------|-------|
|8000   |8      |36     |46     |50     |57     |37     |210    |

### 3T LDBC SNB data
#### Environment 
- 10x GCP n2d-highmem-64 
- Each machine has 64vCPU/512G RAM
- TigerGraph 3.7.0-RC

#### Latency (in millisecond)


### 10T LDBC SNB data
#### Environment 
- 20x GCP n2d-highmem-96 
- Each machine has 96vCPU/768G RAM
- TigerGraph 3.7.0-RC

#### Latency (in millisecond)


