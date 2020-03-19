"""
197. Rising Temperature

Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
For example, return the following Ids for the above Weather table:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+

"""

SELECT Id

FROM (SELECT Id, Temperature - avg_temp as above_avg FROM (SELECT Id, RecordDate, Temperature, AVG(Temperature) OVER (ORDER BY RecordDate RANGE 1 PRECEDING) as avg_temp FROM Weather))

WHERE above_avg > 0
;

'''
Runtime: 911 ms, faster than 62.55% of Oracle online submissions for Rising Temperature.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Rising Temperature.
'''
