package com.amazon.ratingcount;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class RatingCountMapper
        extends Mapper<LongWritable, Text, Text, IntWritable> {

    private static final IntWritable ONE = new IntWritable(1);
    private final Text scoreKey = new Text();

    @Override
    protected void map(
            LongWritable key,
            Text value,
            Context context
    ) throws IOException, InterruptedException {

        String line = value.toString();
        String[] fields = line.split("\t", -1);

        // Expected TSV schema has 10 fields
        if (fields.length >= 10) {

            try {
                int score = Integer.parseInt(fields[6].trim());

                if (score >= 1 && score <= 5) {
                    scoreKey.set(String.valueOf(score));
                    context.write(scoreKey, ONE);
                } else {
                    context.getCounter(
                            "AMAZON_DATA",
                            "INVALID_SCORE"
                    ).increment(1);
                }

            } catch (NumberFormatException e) {
                context.getCounter(
                        "AMAZON_DATA",
                        "INVALID_SCORE"
                ).increment(1);
            }

        } else {
            context.getCounter(
                    "AMAZON_DATA",
                    "MALFORMED_ROWS"
            ).increment(1);
        }
    }
}