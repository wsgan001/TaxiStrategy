'''
Created on Nov 14, 2016

@author: JulianYGao
'''
"""
A library of feature extraction functions. The Rdd_data feed in 
is in the form of 
(date, (Passenger Count, trip time, trip distance, pickup_lon, pickup_lat, 
 dropoff_lon, dropoff_lat, payment_type, fare_amt, extra, mta_tax, 
 tip_amt, tolls_amt, total_amt))
and different feature selections are applied.
Feature extractors will combine feature values within one single day
and produce resulting RDD m x d where m is number of days, and d is number 
of feature dimensions.
"""
from operator import add
import sys
import math

def simple_aggregating_feature_extractor(rdd_data):
    """
    The simple feature extractor only takes account for total passenger count, 
    total trip time in seconds, total trip distance, and total fare amount
    """
    simplified_data = rdd_data.map(lambda (date, feat): (date, (feat[0], \
        feat[1], feat[2], feat[-1])))
    aggregated_data = simplified_data.reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1],\
        a[2] + b[2], a[3] + b[3]))
    return aggregated_data



