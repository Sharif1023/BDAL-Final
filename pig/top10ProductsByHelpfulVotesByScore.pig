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
    AND helpful_num >= 0
    AND score IS NOT NULL
    AND score >= 1
    AND score <= 5;

product_score_group = GROUP valid
    BY (score, productid);

product_totals = FOREACH product_score_group
    GENERATE
        group.score AS score,
        group.productid AS productid,
        SUM(valid.helpful_num) AS total_helpful_votes;

score_group = GROUP product_totals
    BY score;

ranked = FOREACH score_group {
    ordered = ORDER product_totals
        BY total_helpful_votes DESC,
           productid ASC;

    top10 = LIMIT ordered 10;

    GENERATE FLATTEN(top10);
};

STORE ranked
INTO '/amazon/pig_output/top10_products_helpful_by_score'
USING PigStorage('|');