'''
180. Consecutive Numbers

Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
'''

SELECT Num as ConsecutiveNums

FROM (SELECT Num, LEAD(Num, 1) OVER (ORDER BY Id) as next, LAG(Num, 1) OVER (ORDER BY Id) as prev FROM Logs)

WHERE next = Num
AND prev = Num
;

'''
Runtime: 943 ms, faster than 76.37% of Oracle online submissions for Consecutive Numbers.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Consecutive Numbers.
'''
