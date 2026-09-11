package com.amazon.producthelpfulness;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class ProductHelpfulnessReducer
        extends Reducer<Text, IntWritable, Text, LongWritable> {

    @Override
    protected void reduce(
            Text key,
            Iterable<IntWritable> values,
            Context context
    ) throws IOException, InterruptedException {

        long totalHelpfulVotes = 0;

        for (IntWritable value : values) {
            totalHelpfulVotes += value.get();
        }

        context.write(
                key,
                new LongWritable(totalHelpfulVotes)
        );
    }
}