gi-- ================================================
-- Author: fmy
-- Create date: 2024-11-28 
-- Input table: 
-- Output table:
-- Description: 
-- Modify [1]: 
-- Modify [2]: 
-- ================================================
SET spark.app.name=temp.sql;
SET spark.default.parallelism=200;
SET spark.sql.shuffle.partitions=200;
SET spark.driver.cores=2;
SET spark.dirver.memory=4g;
SET spark.executor.cores=4;
SET spark.executor.memory=8g;
SET spark.executor.memoryOverhead=2g;
-- SET spark.executor.instances=10;
SET spark.dynamicAllocation.enabled=true;
SET spark.dynamicAllocation.minExecutors=5;
SET spark.dynamicAllocation.maxExecutors=15;
SET spark.port.maxRetries=100;
-- SET spark.yarn.queue=fmy;
-- SET spark.shuffle.service.enabled=true;