"""
626. Exchange Seats


Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.


Mary wants to change seats for the adjacent students.


Can you write a SQL query to output the result for Mary?


+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+

For the sample input, the output is:


+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+

Note:
If the number of students is odd, there is no need to change the last one's seat.
"""
SELECT RANK() OVER (ORDER BY id) as id, students

FROM SELECT (CASE WHEN mod(id, 2) = 1 THEN id+1 WHEN mod(id,2) = 0 THEN id-1 END as id, student FROM seat ORDER BY id)

ORDER BY id
;

"""
Runtime: 632 ms, faster than 77.95% of Oracle online submissions for Exchange Seats.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Exchange Seats.
"""
