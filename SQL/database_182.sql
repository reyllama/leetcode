'''
182. Duplicate Emails

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
'''

SELECT Email

FROM (
    SELECT distinct Email, COUNT(Id) OVER (PARTITION BY Email) as cnt

    FROM Person
)

WHERE cnt > 1
;

'''
Runtime: 1010 ms, faster than 42.79% of Oracle online submissions for Duplicate Emails.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Duplicate Emails.
'''


SELECT distinct Email

FROM (

SELECT Email, COUNT(Id) OVER (PARTITION BY Email) as cnt

FROM Person

)

WHERE cnt > 1
;

'''
Runtime: 908 ms, faster than 55.02% of Oracle online submissions for Duplicate Emails.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Duplicate Emails.
'''

SELECT Email

FROM (SELECT Email, COUNT(*) as cnt FROM Person GROUP BY Email)

WHERE cnt > 1

'''
Runtime: 605 ms, faster than 92.72% of Oracle online submissions for Duplicate Emails.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Duplicate Emails.
'''
