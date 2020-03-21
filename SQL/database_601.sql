"""
601. Human Traffic of Stadium

X city built a new stadium, each day many people visit it and the stats are saved as these columns: id, visit_date, people

Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).

For example, the table stadium:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
For the sample data above, the output is:

+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
Note:
Each day only have one row record, and the dates are increasing with id increasing.
"""

SELECT id as "id", substr(visit_date, 1, 10) as "visit_date", people as "people"

FROM (SELECT
    id, visit_date, people, LAG(people, 1, 0) OVER (ORDER BY visit_date) as day_minus1, LAG(people, 2, 0) OVER (ORDER BY visit_date) as day_minus2,
    LEAD(people, 1, 0) OVER (ORDER BY visit_date) as day_plus1, LEAD(people, 2, 0) OVER (ORDER BY visit_date) as day_plus2

    FROM stadium
)

WHERE (people>=100 AND day_minus1>=100 And day_minus2>=100)
OR (people>=100 AND day_plus1>=100 AND day_plus2>=100)
OR (people>=100 AND day_minus1>=100 AND day_plus1>=100)
;

"""
Runtime: 583 ms, faster than 97.33% of Oracle online submissions for Human Traffic of Stadium.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Human Traffic of Stadium.
"""
