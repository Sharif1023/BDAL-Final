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
    AND score IS NOT NULL
    AND score >= 1
    AND score <= 5;

clean = FOREACH valid
    GENERATE
        id,
        productid,
        score,
        helpful_num;

grouped = GROUP clean BY score;

ranked = FOREACH grouped {
    ordered = ORDER clean BY helpful_num DESC, id ASC;
    top10 = LIMIT ordered 10;
    GENERATE FLATTEN(top10);
};

STORE ranked
INTO '/amazon/pig_output/top10_helpful_by_score'
USING PigStorage('|');