'''
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
'''

WITH base AS (SELECT Salary, RANK() OVER (ORDER BY Salary DESC) srank FROM Employee),

SELECT Salary as SecondHighestSalary

FROM (SELECT * from base where srank = 2)

;

SELECT Salary as SecondHighestSalary

FROM (SELECT Salary, srank
        FROM (SELECT Salary, RANK() OVER (ORDER BY Salary DESC) as srank FROM Employee)
        WHERE srank = 2
    )
;

SELECT Salary as SecondHighestSalary

FROM (SELECT Salary FROM Employee ORDER BY Salary DESC LIMIT 2) a

ORDER BY Salary

LIMIT 1
;

'RANK FUNCTION DOES NOT seem to work for some reason. Maybe there is an error in my SQL syntax.'

##############################################################################################

'Answer that was accepted.'

SELECT IFNULL((SELECT distinct Salary
FROM Employee
Order by Salary DESC
Limit 1, 1), NULL) AS SecondHighestSalary
