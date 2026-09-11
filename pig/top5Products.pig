reviews = LOAD '/amazon/input/amazon_reviews.tsv'
USING PigStorage('\t')
AS (
    id:long,
    productid:chararray,
    userid:chararray,
    profilename:chararray,
    helpful_num:int,
    helpful_den:int,
    score:int,
    review_time:long,
    summary:chararray,
    review_text:chararray
);

valid = FILTER reviews
    BY productid IS NOT NULL
    AND productid != '';

grouped = GROUP valid BY productid;

counts = FOREACH grouped
    GENERATE
        group AS productid,
        COUNT(valid) AS review_count;

sorted = ORDER counts
    BY review_count DESC;

top5 = LIMIT sorted 5;

STORE top5
INTO '/amazon/pig_output/top5_products'
USING PigStorage('|');