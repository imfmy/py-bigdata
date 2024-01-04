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
       collect_set(name) AS names
  FROM t
 GROUP BY pid

