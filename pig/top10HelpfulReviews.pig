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
    BY id IS NOT NULL
    AND productid IS NOT NULL
    AND helpful_num IS NOT NULL
    AND score IS NOT NULL;

ordered = ORDER valid
    BY helpful_num DESC;

top10 = LIMIT ordered 10;

result = FOREACH top10
    GENERATE
        id,
        productid,
        score,
        helpful_num;

STORE result
INTO '/amazon/pig_output/top10_helpful_reviews'
USING PigStorage('|');