package com.amazon.producthelpfulness;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class ProductHelpfulnessMapper
        extends Mapper<LongWritable, Text, Text, IntWritable> {

    private final Text productId = new Text();
    private final IntWritable helpfulVotes = new IntWritable();

    @Override
    protected void map(
            LongWritable key,
            Text value,
            Context context
    ) throws IOException, InterruptedException {

        String line = value.toString();
        String[] fields = line.split("\t", -1);

        if (fields.length >= 10) {

            String product = fields[1].trim();

            try {
                int helpful =
                        Integer.parseInt(fields[4].trim());

                if (!product.isEmpty() && helpful >= 0) {

                    productId.set(product);
                    helpfulVotes.set(helpful);

                    context.write(
                            productId,
                            helpfulVotes
                    );

                } else {

                    context.getCounter(
                            "AMAZON_DATA",
                            "INVALID_PRODUCT_OR_HELPFULNESS"
                    ).increment(1);
                }

            } catch (NumberFormatException e) {

                context.getCounter(
                        "AMAZON_DATA",
                        "INVALID_HELPFULNESS"
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