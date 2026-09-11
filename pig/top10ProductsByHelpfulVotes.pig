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
    AND productid != ''
    AND helpful_num IS NOT NULL
    AND helpful_num >= 0;

grouped = GROUP valid BY productid;

totals = FOREACH grouped
    GENERATE
        group AS productid,
        SUM(valid.helpful_num) AS total_helpful_votes;

ordered = ORDER totals
    BY total_helpful_votes DESC;

top10 = LIMIT ordered 10;

STORE top10
INTO '/amazon/pig_output/top10_products_helpful'
USING PigStorage('|');