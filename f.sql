-- ssh://zhaomin@10.2.3.1:40022/usr/bin/python3 -u /home/zhaomin/lxy-data-warehouse/bin/spark-ods-dwd-full-update-starter.py -c conf/validation/b2b_info/full-update_starter/tender_relation_info.json -dt 20220628-20220629
-- /home/zhaomin/lxy-data-warehouse/bin/common/functions.sh: line 4: syntax error near unexpected token `$'{\r''
-- '
-- 2022-07-12 15:46:20 Project lxy-data-warehouse is running in normal user zhaomin
-- 2022-07-12 15:46:20 Project lxy-data-warehouse is running in normal user dir /home/zhaomin/lxy-data-warehouse
-- Ticket cache: FILE:/tmp/krb5cc_2017
-- Default principal: alvis@LIXIAOYUN.COM
--
-- Valid starting       Expires              Service principal
-- 07/12/2022 15:46:20  07/13/2022 15:46:20  krbtgt/LIXIAOYUN.COM@LIXIAOYUN.COM
-- 	renew until 07/19/2022 15:46:20
-- 2022-07-12 15:46:20 /home/zhaomin/lxy-data-warehouse/bin/spark-ods-dwd-full-update-starter.py 收到参数：-c conf/validation/b2b_info/full-update_starter/tender_relation_info.json -dt 20220628-20220629
-- 2022-07-12 15:46:20 解析到参数： c => conf/validation/b2b_info/full-update_starter/tender_relation_info.json
-- 2022-07-12 15:46:20 解析到参数： dt => 20220628-20220629
-- 2022-07-12 15:46:20 ODS-DWD Spark config  : spark.driver.memory => 2g
-- 2022-07-12 15:46:20 ODS-DWD Spark config  : spark.executor.memory => 2g
-- 2022-07-12 15:46:20 ODS-DWD Spark config  : spark.driver.cores => 4
-- 2022-07-12 15:46:20 ODS-DWD Spark config  : spark.executor.cores => 4
-- 2022-07-12 15:46:20 ODS-DWD Spark config  : spark.executor.instances => 2
-- 2022-07-12 15:46:20 ODS-DWD Spark config  : spark.executor.memoryOverhead => 2048
-- 2022-07-12 15:46:20 Spark UDF file       : lxy/spark/udf/spark_common_udf.py
-- 2022-07-12 15:46:20 Spark UDF file       : lxy/validation/validator/json_schema_validator_spark.py
-- 2022-07-12 15:46:20 使用日期20220628 运行ODS-DWD 全量合并作业，目标表 crl_dwd.dwd_crl_tender_relation_info
-- 2022-07-12 15:46:20 SQL_SCRIPT_TEMPLATE     : /home/zhaomin/lxy-data-warehouse/conf/template/spark/ods-dwd-full-update-template.sql
-- 2022-07-12 15:46:20 JOB_CONFIG_PATH         : /home/zhaomin/lxy-data-warehouse/conf/validation/b2b_info/full-update_starter/tender_relation_info.json
-- 2022-07-12 15:46:20 ODS_TABLE               : crl_ods.ods_crl_tender_relation_info
-- 2022-07-12 15:46:20 DWD_TABLE               : crl_dwd.dwd_crl_tender_relation_info
-- 2022-07-12 15:46:20 PK_FIELDS               : tender_type, pid, project_name, web_name
-- 2022-07-12 15:46:20 PARTITION_BY_PK_FIELDS  : nvl(tender_type,""), nvl(pid,""), nvl(project_name,""), nvl(web_name,"")
-- 2022-07-12 15:46:20 CONVERTED_ODS_FIELDS    : tender_type, pid, project_name, web_name, table_name, company_name, cast(public_date as BIGINT) as public_date, project_id, region, url, contract_type, html_cache_id, json_cache_id, url_desc, crawler_time
-- 2022-07-12 15:46:20 TDY_ALL_PK_FIELD_IS_NULL: tdy.tender_type IS NULL AND tdy.pid IS NULL AND tdy.project_name IS NULL AND tdy.web_name IS NULL
-- 2022-07-12 15:46:20 YST_ALL_PK_FIELD_IS_NULL: yst.tender_type IS NULL AND yst.pid IS NULL AND yst.project_name IS NULL AND yst.web_name IS NULL
-- 2022-07-12 15:46:20 TDY_PK_FIELDS           : tdy.tender_type, tdy.pid, tdy.project_name, tdy.web_name
-- 2022-07-12 15:46:20 YST_PK_FIELDS           : yst.tender_type, yst.pid, yst.project_name, yst.web_name
-- 2022-07-12 15:46:20 PK_FIELDS_JOIN_EXPR     : tdy.tender_type <=> yst.tender_type AND tdy.pid <=> yst.pid AND tdy.project_name <=> yst.project_name AND tdy.web_name <=> yst.web_name
-- 2022-07-12 15:46:20 OTHER_FIELDS            : table_name, company_name, public_date, project_id, region, url, contract_type, html_cache_id, json_cache_id, url_desc
-- 2022-07-12 15:46:20 TDY_OTHER_FIELDS        : tdy.table_name, tdy.company_name, tdy.public_date, tdy.project_id, tdy.region, tdy.url, tdy.contract_type, tdy.html_cache_id, tdy.json_cache_id, tdy.url_desc
-- 2022-07-12 15:46:20 YST_OTHER_FIELDS        : yst.table_name, yst.company_name, yst.public_date, yst.project_id, yst.region, yst.url, yst.contract_type, yst.html_cache_id, yst.json_cache_id, yst.url_desc
-- 2022-07-12 15:46:20 OTHER_FIELDS_NVL_EXPR   : nvl(tdy.table_name, yst.table_name), nvl(tdy.company_name, yst.company_name), nvl(tdy.public_date, yst.public_date), nvl(tdy.project_id, yst.project_id), nvl(tdy.region, yst.region), nvl(tdy.url, yst.url), nvl(tdy.contract_type, yst.contract_type), nvl(tdy.html_cache_id, yst.html_cache_id), nvl(tdy.json_cache_id, yst.json_cache_id), nvl(tdy.url_desc, yst.url_desc)
-- 2022-07-12 15:46:20 IS_UPDATE_EXPR          : tdy.table_name <=> yst.table_name AND tdy.company_name <=> yst.company_name AND tdy.public_date <=> yst.public_date AND tdy.project_id <=> yst.project_id AND tdy.region <=> yst.region AND tdy.url <=> yst.url AND tdy.contract_type <=> yst.contract_type AND tdy.html_cache_id <=> yst.html_cache_id AND tdy.json_cache_id <=> yst.json_cache_id AND tdy.url_desc <=> yst.url_desc
-- 2022-07-12 15:46:20 VALID_EXPR              : valid
-- 2022-07-12 15:46:20 TIME_FIELD              : crawler_time
-- 2022-07-12 15:46:20 dt                      : 20220628
-- 2022-07-12 15:46:20 RESULT_PARTITIONS       : 1
-- 2022-07-12 15:46:20 替换参数后的SQL如下:
-- -- ==================================================
-- -- Author: stuart alex
-- -- Create date: 2021/7/22
-- -- Input table: crl_ods.ods_crl_tender_relation_info, crl_dwd.dwd_crl_tender_relation_info
-- -- Output table: crl_dwd.dwd_crl_tender_relation_info
-- -- Description: ODS-DWD昨日全量和今日增量去重合并的SQL模板，需要注意的时，字段的组织要符合主键字段在前、其他字段在中、时间字段最后。
-- -- Modify [1]:
-- -- Modify [2]:
-- -- Parameter:
-- -- ODS_TABLE: ODS表名称
-- -- DWD_TABLE: DWD表名称
-- -- VALID_EXPR: ODS层有效数据筛选表达式
-- -- PK_FIELDS: 主键字段（支持多个）
-- -- TDY_ALL_PK_FIELD_IS_NULL: 用来进行左连接或右连接后，剔除数据的主键（由于主键允许为空，需所有主键字段参与判断）
-- -- YST_ALL_PK_FIELD_IS_NULL: 用来进行左连接或右连接后，剔除数据的主键（由于主键允许为空，需所有主键字段参与判断）
-- -- TDY_PK_FIELDS: 附加了表别名的主键，例如tdy.id、tdy.name，其中tdy为限定别名
-- -- YST_PK_FIELDS: 附加了表别名的主键，例如yst.id、yst.name，其中yst为限定别名
-- -- PK_FIELDS_JOIN_EXPR: 主键JOIN表达式，例如tdy.id = yst.id and tdy.name = yst.name
-- -- OTHER_FIELDS: 其他非主键、非时间的字段（可多个）
-- -- TDY_OTHER_FIELDS: 附加了表别名的其他非主键、非时间的字段（可多个），例如tdy.col1, tdy.col2，其中tdy为限定别名
-- -- YST_OTHER_FIELDS: 附加了表别名的其他非主键、非时间的字段（可多个），例如yst.col1, yst.col2，其中tdy为限定别名
-- -- OTHER_FIELDS_NVL_EXPR: 更新旧值的表达式，例如nvl(yst.col1, tdy.col1), nvl(yst.col2, tdy.col2)，其中tdy、yst为限定别名
-- -- TIME_FIELD: 时间字段，新增数据去重用来进行排序（倒序）的字段，例如crawler_time
-- -- dt: 日期
-- -- ==================================================
WITH inc AS (
    -- 今日增量数据
    SELECT tender_type, pid, project_name, web_name,
           table_name, company_name, public_date, project_id, region, url, contract_type, html_cache_id, json_cache_id, url_desc,
           crawler_time,
           row_number() OVER (PARTITION BY nvl(tender_type,""), nvl(pid,""), nvl(project_name,""), nvl(web_name,"") ORDER BY crawler_time DESC) as row_number
      FROM crl_ods.ods_crl_tender_relation_info
     WHERE dt = '20220628' AND valid
),
     tdy AS (
    SELECT tender_type, pid, project_name, web_name, table_name, company_name, cast(public_date as BIGINT) as public_date, project_id, region, url, contract_type, html_cache_id, json_cache_id, url_desc, crawler_time
      FROM inc
     WHERE row_number=1
),
     yst AS (
    -- 昨日全量数据
    SELECT create_date,
           update_date,
           tender_type, pid, project_name, web_name,
           table_name, company_name, public_date, project_id, region, url, contract_type, html_cache_id, json_cache_id, url_desc
      FROM crl_dwd.dwd_crl_tender_relation_info
     WHERE dt = date_format(date_add(from_unixtime(to_unix_timestamp('20220628','yyyyMMdd')),-1),'yyyyMMdd')
),
     old AS (
    -- 昨日数据（A）不在今日数据（B）中的部分：A-B
    SELECT yst.create_date,
           yst.update_date,
           'old' AS record_status,
           yst.tender_type, yst.pid, yst.project_name, yst.web_name,
           yst.table_name, yst.company_name, yst.public_date, yst.project_id, yst.region, yst.url, yst.contract_type, yst.html_cache_id, yst.json_cache_id, yst.url_desc
      FROM yst
      LEFT JOIN tdy
        ON tdy.tender_type <=> yst.tender_type AND tdy.pid <=> yst.pid AND tdy.project_name <=> yst.project_name AND tdy.web_name <=> yst.web_name
     WHERE tdy.tender_type IS NULL AND tdy.pid IS NULL AND tdy.project_name IS NULL AND tdy.web_name IS NULL
),
     upd AS (
    -- 昨日数据（A）与今日数据（B）重叠的部分：A∩B
    SELECT nvl(yst.create_date,tdy.crawler_time) AS create_date,
           nvl(tdy.crawler_time, yst.update_date) AS update_date,
           if(tdy.table_name <=> yst.table_name AND tdy.company_name <=> yst.company_name AND tdy.public_date <=> yst.public_date AND tdy.project_id <=> yst.project_id AND tdy.region <=> yst.region AND tdy.url <=> yst.url AND tdy.contract_type <=> yst.contract_type AND tdy.html_cache_id <=> yst.html_cache_id AND tdy.json_cache_id <=> yst.json_cache_id AND tdy.url_desc <=> yst.url_desc,'no-change','updated') AS record_status,
           yst.tender_type, yst.pid, yst.project_name, yst.web_name,
           nvl(tdy.table_name, yst.table_name), nvl(tdy.company_name, yst.company_name), nvl(tdy.public_date, yst.public_date), nvl(tdy.project_id, yst.project_id), nvl(tdy.region, yst.region), nvl(tdy.url, yst.url), nvl(tdy.contract_type, yst.contract_type), nvl(tdy.html_cache_id, yst.html_cache_id), nvl(tdy.json_cache_id, yst.json_cache_id), nvl(tdy.url_desc, yst.url_desc)
      FROM yst
      JOIN tdy
        ON tdy.tender_type <=> yst.tender_type AND tdy.pid <=> yst.pid AND tdy.project_name <=> yst.project_name AND tdy.web_name <=> yst.web_name
),
     new AS (
    -- 今日数据（B）不在昨日数据（A）中的部分：B-A
    SELECT tdy.crawler_time AS create_date,
           tdy.crawler_time AS update_date,
           'new' as record_status,
           tdy.tender_type, tdy.pid, tdy.project_name, tdy.web_name,
           tdy.table_name, tdy.company_name, tdy.public_date, tdy.project_id, tdy.region, tdy.url, tdy.contract_type, tdy.html_cache_id, tdy.json_cache_id, tdy.url_desc
      FROM tdy
      LEFT JOIN yst
        ON tdy.tender_type <=> yst.tender_type AND tdy.pid <=> yst.pid AND tdy.project_name <=> yst.project_name AND tdy.web_name <=> yst.web_name
     WHERE yst.tender_type IS NULL AND yst.pid IS NULL AND yst.project_name IS NULL AND yst.web_name IS NULL
),
     und AS (
    SELECT * FROM old
     UNION ALL
    SELECT * FROM upd
     UNION ALL
    SELECT * FROM new
)
INSERT OVERWRITE TABLE crl_dwd.dwd_crl_tender_relation_info PARTITION (dt = '20220628')
SELECT /*+ REPARTITION(1) */* FROM und
--
-- 2022-07-12 15:46:20 基于用户 zhaomin 创建 SparkSession
-- 2022-07-12 15:46:20 添加自定义 Spark 配置 spark.driver.memory => 2g
-- 2022-07-12 15:46:20 添加自定义 Spark 配置 spark.executor.memory => 2g
-- 2022-07-12 15:46:20 添加自定义 Spark 配置 spark.driver.cores => 4
-- 2022-07-12 15:46:20 添加自定义 Spark 配置 spark.executor.cores => 4
-- 2022-07-12 15:46:20 添加自定义 Spark 配置 spark.executor.instances => 2
-- 2022-07-12 15:46:20 添加自定义 Spark 配置 spark.executor.memoryOverhead => 2048
-- 2022-07-12 15:46:20 创建 SparkSession