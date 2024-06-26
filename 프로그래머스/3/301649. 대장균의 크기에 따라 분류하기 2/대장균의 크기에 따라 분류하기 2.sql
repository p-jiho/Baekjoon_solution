with NEW as(
select ID, PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS SIZE
from ECOLI_DATA
)

select E.ID, CASE WHEN N.SIZE <= 0.25 THEN 'CRITICAL'
                WHEN N.SIZE <= 0.5 THEN "HIGH"
                WHEN N.SIZE <= 0.75 THEN "MEDIUM"
                ELSE "LOW" END AS COLONY_NAME
from ECOLI_DATA E, NEW N
WHERE E.ID = N.ID
ORDER BY ID ASC