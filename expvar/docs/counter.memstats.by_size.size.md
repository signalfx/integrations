---
title: memstats.by_size.size
brief: The maximum byte size of a class as identified by dimension class
metric_type: counter
---
### memstats.by_size.size

The maximum byte size of a class as identified by dimension class. It is the class interval upper limit. The values of dimension class are numbers between 0 and 60 inclusive. Consecutive classes are of consecutive dimension class values. The lower limit of a class is the upper limit of the consecutive class below. Metrics memstats.by_size.size, memstats.by_size.mallocs and memstats.by_size.frees of the same class are related