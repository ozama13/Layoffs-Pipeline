#Athena Queries

SELECT
    company_name,
    SUM(layoffs_count) AS total_layoffs
FROM layoffs_hiring_db.hiring_trends
GROUP BY company_name
ORDER BY total_layoffs DESC
LIMIT 10;

SELECT
    industry,
    SUM(layoffs_count) AS total_layoffs
FROM layoffs_hiring_db.hiring_trends
GROUP BY industry
ORDER BY total_layoffs DESC;

SELECT
    industry,
    AVG(ai_replacement_risk) AS avg_ai_risk
FROM layoffs_hiring_db.hiring_trends
GROUP BY industry
ORDER BY avg_ai_risk DESC;

SELECT
    company_name,
    SUM(layoffs_count) AS total_layoffs
FROM layoffs_hiring_db.hiring_trends
GROUP BY company_name
ORDER BY total_layoffs DESC
LIMIT 10;

SELECT
    year,
    SUM(open_roles) AS total_open_roles,
    SUM(layoffs_count) AS total_layoffs
FROM layoffs_hiring_db.hiring_trends
GROUP BY year
ORDER BY year;

