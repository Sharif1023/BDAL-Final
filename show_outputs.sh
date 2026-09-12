#!/bin/bash

clear

echo "================================================================"
echo " AMAZON FINE FOOD REVIEWS - FINAL OUTPUT DEMO"
echo " Ubuntu / WSL"
echo "================================================================"

echo
echo "MAPREDUCE 1 - BEST REVIEWER TOP 10"
echo "----------------------------------------------------------------"
cat results/mapreduce/mr1_top10_reviewers.txt

echo
echo "MAPREDUCE 2 - TOTAL REVIEWS BY RATING SCORE"
echo "----------------------------------------------------------------"
cat results/mapreduce/mr2_rating_count.txt

echo
echo "MAPREDUCE 3 - TOP PRODUCTS BY TOTAL HELPFUL VOTES"
echo "----------------------------------------------------------------"
cat results/mapreduce/mr3_top10_product_helpfulness.txt

echo
echo "PIG 1 - TOP 5 PRODUCTS BY NUMBER OF REVIEWS"
echo "----------------------------------------------------------------"
cat results/pig/pig1_top5_products.txt

echo
echo "PIG 2 - TOP 10 MOST HELPFUL REVIEWS"
echo "----------------------------------------------------------------"
cat results/pig/pig2_top10_helpful_reviews.txt

echo
echo "PIG 3 - TOP 10 HELPFUL REVIEWS BY RATING SCORE"
echo "----------------------------------------------------------------"
cat results/pig/pig3_top10_helpful_by_score.txt

echo
echo "PIG 4 - TOP 10 PRODUCTS BY TOTAL HELPFUL VOTES"
echo "----------------------------------------------------------------"
cat results/pig/pig4_top10_products_helpful.txt

echo
echo "PIG 5 - TOP 10 PRODUCTS BY HELPFUL VOTES FOR EACH SCORE"
echo "----------------------------------------------------------------"
cat results/pig/pig5_top10_products_helpful_by_score.txt

echo
echo "================================================================"
echo " END OF FINAL OUTPUTS"
echo "================================================================"

