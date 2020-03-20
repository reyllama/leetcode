"""
596. Classes More Than 5 Students

There is a table courses with columns: student and class

Please list out all classes which have more than or equal to 5 students.

For example, the table:

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
Should output:

+---------+
| class   |
+---------+
| Math    |
+---------+
"""

SELECT class

FROM (SELECT class, count(*) as cnt FROM courses group by 1)

WHERE cnt >=5
;

"""
Runtime: 694 ms, faster than 62.56% of Oracle online submissions for Classes More Than 5 Students.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Classes More Than 5 Students.
"""
