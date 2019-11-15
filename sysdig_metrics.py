# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

class Metric:
    def __init__(self, metricType, valueType, segmentBy, defaultTimeAggregation, timeAggregationFormat, defaultGroupAggregation, groupAggregationFormat):
        self.metricType = metricType
        self.valueType = valueType
        self.segmentBy = segmentBy
        self.defaultTimeAggregation = defaultTimeAggregation
        self.timeAggregationFormat = timeAggregationFormat
        self.defaultGroupAggregation = defaultGroupAggregation
        self.groupAggregationFormat = groupAggregationFormat
 
           