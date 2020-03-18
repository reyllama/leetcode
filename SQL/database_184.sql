'''
184. Department Highest Salary

The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
'''

SELECT Department, Employee, Salary

FROM (SELECT Id, Name as Employee, Salary, DepartmentId, RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) as sal_rank FROM Employee) a
LEFT JOIN (SELECT Id as dId, Name as Department FROM Department) b
ON a.DepartmentId = b.dId

WHERE sal_rank = 1

;

'''
Runtime: 1066 ms, faster than 73.64% of Oracle online submissions for Department Highest Salary.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Department Highest Salary.
'''
