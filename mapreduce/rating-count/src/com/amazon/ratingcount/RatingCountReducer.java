package com.amazon.ratingcount;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class RatingCountReducer
        extends Reducer<Text, IntWritable, Text, IntWritable> {

    @Override
    protected void reduce(
            Text key,
            Iterable<IntWritable> values,
            Context context
    ) throws IOException, InterruptedException {

        int totalReviews = 0;

        for (IntWritable value : values) {
            totalReviews += value.get();
        }

        context.write(
                key,
                new IntWritable(totalReviews)
        );
    }
}