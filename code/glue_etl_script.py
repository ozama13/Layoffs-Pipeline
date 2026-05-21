import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1779240063887 = glueContext.create_dynamic_frame.from_catalog(database="layoffs_hiring_db", table_name="hiring_trends", transformation_ctx="AWSGlueDataCatalog_node1779240063887")

# Script generated for node Drop Duplicates
DropDuplicates_node1779240220145 =  DynamicFrame.fromDF(AWSGlueDataCatalog_node1779240063887.toDF().dropDuplicates(), glueContext, "DropDuplicates_node1779240220145")

# Script generated for node Change Schema
ChangeSchema_node1779240265414 = ApplyMapping.apply(frame=DropDuplicates_node1779240220145, mappings=[("record_id", "string", "record_id", "string"), ("company_name", "string", "company_name", "string"), ("industry", "string", "industry", "string"), ("country", "string", "country", "string"), ("company_size", "string", "company_size", "string"), ("month", "string", "month", "string"), ("year", "long", "year", "long"), ("layoffs_count", "long", "layoffs_count", "int"), ("layoff_percentage", "double", "layoff_percentage", "double"), ("reason_for_layoffs", "string", "reason_for_layoffs", "string"), ("ai_automation_impact", "double", "ai_automation_impact", "double"), ("ai_replacement_risk", "double", "ai_replacement_risk", "double"), ("open_roles", "long", "open_roles", "int"), ("hiring_trend", "string", "hiring_trend", "string"), ("remote_jobs_percentage", "double", "remote_jobs_percentage", "double"), ("top_hiring_role", "string", "top_hiring_role", "string"), ("stock_growth_percent", "double", "stock_growth_percent", "double"), ("revenue_growth_percent", "double", "revenue_growth_percent", "double"), ("salary_budget_change", "double", "salary_budget_change", "double"), ("ai_adoption_level", "double", "ai_adoption_level", "double"), ("employee_sentiment", "double", "employee_sentiment", "double"), ("job_security_score", "double", "job_security_score", "double"), ("market_condition", "string", "market_condition", "string")], transformation_ctx="ChangeSchema_node1779240265414")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1779240265414, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1779240049068", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1779240608713 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1779240265414, connection_type="s3", format="glueparquet", connection_options={"path": "s3://layoffs-bucket/curated/tech_layoffs/hiring_trends/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1779240608713")

job.commit()
