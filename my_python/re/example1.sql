-- ================================================
-- Author: fmy
-- Create date: 2023-07-20 
-- Input table: 
-- Output table:
-- Description: 
-- Modify [1]: 
-- Modify [2]: 
-- ================================================
SELECT pid,
       collect_set(name) AS names,
       collect_set(age) AS ages,
       size(gender) AS gender_size,
       size(gender1) AS gender1,
       current_date() AS c_date,
       1<=>NULL AS is_eq
  FROM t
 GROUP BY pid
;
SELECT 1 <=> 1 AS c1, 1 <=> 2 AS c2, 1 <=> NULL AS c3, NULL <=> NULL AS c4
