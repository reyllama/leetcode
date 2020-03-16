'''
183. Customers Who Never Order

Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
'''

SELECT Name as Customers

FROM Customers a left join (SELECT Id as Order_id, CustomerId FROM Orders) b on a.Id = b.CustomerId

WHERE Order_id IS NULL

;

'''
Runtime: 1486 ms, faster than 29.95% of Oracle online submissions for Customers Who Never Order.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Customers Who Never Order.
'''

WITH base as
(SELECT Id, Name FROM Customers

MINUS

SELECT Customers.Id, Name FROM Orders left join Customers on Orders.CustomerId = Customers.Id
)

SELECT Name as Customers From base
;

'''
Runtime: 803 ms, faster than 89.30% of Oracle online submissions for Customers Who Never Order.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Customers Who Never Order.
'''
