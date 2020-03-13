# Write your MySQL query statement below

''' SIMPLE OUTER JOIN PROBLEM - SELECT 4 Fields from these two tables, whether the address info exists or not.

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+

AddressId is the primary key column for this table.
PersonId is the primary key column for this table.
'''

SELECT FirstName
    , Lastname
    , City
    , State

FROM (SELECT PersonId, FirstName, LastName From Person) a
LEFT JOIN (SELECT PersonId, City, State From Address) b
ON a.PersonId = b.PersonId;
