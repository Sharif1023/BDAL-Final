@echo off
setlocal
title Amazon Fine Food Hadoop - Start + Final Demo
cd /d C:\Users\shari\Amazon-Fine-Food-Hadoop

cls
echo ================================================================
echo AMAZON FINE FOOD REVIEWS - START HADOOP + FINAL OUTPUT DEMO
echo ================================================================
echo.
echo Starting HDFS...
call C:\hadoop\sbin\start-dfs.cmd
echo Starting YARN...
call C:\hadoop\sbin\start-yarn.cmd
echo Starting JobHistoryServer in a separate window...
start "JobHistoryServer" cmd /k "cd /d C:\hadoop\bin && mapred historyserver"
timeout /t 8 /nobreak >nul

echo.
echo [1] Hadoop process check
echo ----------------------------------------------------------------
jps
echo.

echo [2] HDFS input check
echo ----------------------------------------------------------------
hdfs dfs -ls -h /amazon/input
echo.

echo ================================================================
echo MAPREDUCE 1 - BEST REVIEWER (TOP 10)
echo ================================================================
type results\mapreduce\mr1_top10_reviewers.txt
echo.

echo ================================================================
echo MAPREDUCE 2 - TOTAL REVIEWS BY RATING SCORE
echo ================================================================
type results\mapreduce\mr2_rating_count.txt
echo.

echo ================================================================
echo MAPREDUCE 3 - TOP PRODUCTS BY TOTAL HELPFUL VOTES
echo ================================================================
type results\mapreduce\mr3_top10_product_helpfulness.txt
echo.

echo ================================================================
echo PIG 1 - TOP 5 PRODUCTS BY NUMBER OF REVIEWS
echo ================================================================
type results\pig\pig1_top5_products.txt
echo.

echo ================================================================
echo PIG 2 - TOP 10 MOST HELPFUL REVIEWS
echo ================================================================
type results\pig\pig2_top10_helpful_reviews.txt
echo.

echo ================================================================
echo PIG 3 - TOP 10 HELPFUL REVIEWS BY RATING SCORE
echo ================================================================
type results\pig\pig3_top10_helpful_by_score.txt
echo.

echo ================================================================
echo PIG 4 - TOP 10 PRODUCTS BY TOTAL HELPFUL VOTES
echo ================================================================
type results\pig\pig4_top10_products_helpful.txt
echo.

echo ================================================================
echo PIG 5 - TOP 10 PRODUCTS BY HELPFUL VOTES FOR EACH SCORE
echo ================================================================
type results\pig\pig5_top10_products_helpful_by_score.txt
echo.

echo ================================================================
echo END OF FINAL OUTPUTS
echo ================================================================
echo JobHistoryServer remains open in its own CMD window.
pause
endlocal
