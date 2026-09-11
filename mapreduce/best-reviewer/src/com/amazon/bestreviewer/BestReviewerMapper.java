package com.amazon.bestreviewer;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class BestReviewerMapper
        extends Mapper<LongWritable, Text, Text, IntWritable> {

    private static final IntWritable ONE = new IntWritable(1);
    private final Text userId = new Text();

    @Override
    protected void map(
            LongWritable key,
            Text value,
            Context context
    ) throws IOException, InterruptedException {

        String line = value.toString();

        String[] fields = line.split("\t", -1);

        // Expected schema contains 10 fields.
        if (fields.length >= 10) {

            String user = fields[2].trim();

            if (!user.isEmpty()) {
                userId.set(user);
                context.write(userId, ONE);
            } else {
                context.getCounter(
                        "AMAZON_DATA",
                        "EMPTY_USER_ID"
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