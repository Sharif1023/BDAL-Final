import csv
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE = os.path.join(
    PROJECT_ROOT,
    "dataset",
    "Reviews.csv"
)

OUTPUT_FILE = os.path.join(
    PROJECT_ROOT,
    "dataset",
    "amazon_reviews.tsv"
)

SAMPLE_FILE = os.path.join(
    PROJECT_ROOT,
    "dataset",
    "sample_amazon_reviews.tsv"
)

SUMMARY_FILE = os.path.join(
    PROJECT_ROOT,
    "dataset",
    "preprocessing_summary.txt"
)

EXPECTED_COLUMNS = [
    "Id",
    "ProductId",
    "UserId",
    "ProfileName",
    "HelpfulnessNumerator",
    "HelpfulnessDenominator",
    "Score",
    "Time",
    "Summary",
    "Text",
]


def clean_text(value):
    if value is None:
        return ""

    value = str(value)

    # TSV এবং Hadoop parsing safe রাখার জন্য
    value = value.replace("\t", " ")
    value = value.replace("\r", " ")
    value = value.replace("\n", " ")

    # Multiple spaces clean করা
    value = " ".join(value.split())

    return value.strip()


total_rows = 0
valid_rows = 0
invalid_rows = 0
sample_limit = 20


print("Amazon Fine Food Reviews Dataset Preprocessing")
print("=" * 55)
print(f"Input : {INPUT_FILE}")
print(f"Output: {OUTPUT_FILE}")
print()


with open(
    INPUT_FILE,
    "r",
    encoding="utf-8",
    errors="replace",
    newline=""
) as infile, open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8",
    newline=""
) as outfile, open(
    SAMPLE_FILE,
    "w",
    encoding="utf-8",
    newline=""
) as samplefile:

    reader = csv.DictReader(infile)

    if reader.fieldnames != EXPECTED_COLUMNS:
        print("WARNING: CSV columns are different from the expected schema.")
        print("Detected columns:")
        print(reader.fieldnames)

    writer = csv.writer(
        outfile,
        delimiter="\t",
        lineterminator="\n",
        quoting=csv.QUOTE_MINIMAL
    )

    sample_writer = csv.writer(
        samplefile,
        delimiter="\t",
        lineterminator="\n",
        quoting=csv.QUOTE_MINIMAL
    )

    for row in reader:

        total_rows += 1

        try:
            review_id = clean_text(row["Id"])
            product_id = clean_text(row["ProductId"])
            user_id = clean_text(row["UserId"])
            profile_name = clean_text(row["ProfileName"])

            helpful_num = int(row["HelpfulnessNumerator"])
            helpful_den = int(row["HelpfulnessDenominator"])
            score = int(row["Score"])
            review_time = int(row["Time"])

            summary = clean_text(row["Summary"])
            review_text = clean_text(row["Text"])

            # Required values check
            if not review_id or not product_id or not user_id:
                invalid_rows += 1
                continue

            # Basic numeric validation
            if helpful_num < 0:
                invalid_rows += 1
                continue

            if helpful_den < 0:
                invalid_rows += 1
                continue

            if helpful_num > helpful_den:
                invalid_rows += 1
                continue

            if score < 1 or score > 5:
                invalid_rows += 1
                continue

            cleaned_row = [
                review_id,
                product_id,
                user_id,
                profile_name,
                helpful_num,
                helpful_den,
                score,
                review_time,
                summary,
                review_text,
            ]

            writer.writerow(cleaned_row)

            if valid_rows < sample_limit:
                sample_writer.writerow(cleaned_row)

            valid_rows += 1

        except (
            ValueError,
            TypeError,
            KeyError
        ):
            invalid_rows += 1

        if total_rows % 50000 == 0:
            print(
                f"Processed: {total_rows:,} | "
                f"Valid: {valid_rows:,} | "
                f"Invalid: {invalid_rows:,}"
            )


with open(
    SUMMARY_FILE,
    "w",
    encoding="utf-8"
) as summary:
    summary.write("Amazon Fine Food Reviews - Preprocessing Summary\n")
    summary.write("=" * 50 + "\n")
    summary.write(f"Total CSV records : {total_rows:,}\n")
    summary.write(f"Valid records     : {valid_rows:,}\n")
    summary.write(f"Invalid records   : {invalid_rows:,}\n")
    summary.write(f"Output file       : amazon_reviews.tsv\n")
    summary.write(
        f"Output size       : "
        f"{os.path.getsize(OUTPUT_FILE):,} bytes\n"
    )


print()
print("=" * 55)
print("PREPROCESSING COMPLETED")
print("=" * 55)
print(f"Total records : {total_rows:,}")
print(f"Valid records : {valid_rows:,}")
print(f"Invalid rows  : {invalid_rows:,}")
print(
    f"Output size   : "
    f"{os.path.getsize(OUTPUT_FILE):,} bytes"
)
print()
print("Generated files:")
print("1. amazon_reviews.tsv")
print("2. sample_amazon_reviews.tsv")
print("3. preprocessing_summary.txt")