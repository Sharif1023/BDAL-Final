# Amazon Fine Food Reviews Data Analysis Using Hadoop

Big Data analysis of the **Amazon Fine Food Reviews** dataset using **Hadoop HDFS, Java MapReduce, Apache Pig, and Python-based visualization**.

The project processes **568,452 valid Amazon food review records**, performs **three Java MapReduce analyses** and **five Apache Pig analyses**, stores the cleaned dataset in HDFS, saves analytical outputs, and generates visualizations for the final report.

**Project Repository:** https://github.com/Sharif1023/BDAL-Final

---

## Project Objectives

The objectives of this project are:

- Store a large Amazon review dataset using Hadoop HDFS.
- Clean and convert the original CSV dataset into a Hadoop-friendly TSV format.
- Process and summarize review data using Java MapReduce.
- Perform higher-level analytical queries using Apache Pig.
- Identify important patterns related to reviewers, ratings, products, and helpful votes.
- Generate visualizations from the analytical results.
- Demonstrate a complete Hadoop-based Big Data Analytics workflow.

---

## Dataset

**Dataset:** Amazon Fine Food Reviews  
**Source:** https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews

| Item | Value |
|---|---:|
| Original records | 568,454 |
| Valid records after preprocessing | 568,452 |
| Invalid records removed | 2 |
| Cleaned dataset size | 299,117,356 bytes |
| HDFS input location | `/amazon/input/amazon_reviews.tsv` |

The original CSV contains review text, summaries, commas, quotation marks, and possible line breaks. To make the dataset easier and safer to process with Hadoop, it was converted into a **tab-separated TSV file** before running the MapReduce and Pig jobs.

### Dataset Fields

| Field | Description |
|---|---|
| `Id` | Unique review identifier |
| `ProductId` | Amazon product identifier |
| `UserId` | Unique reviewer identifier |
| `ProfileName` | Reviewer profile name |
| `HelpfulnessNumerator` | Number of users who found the review helpful |
| `HelpfulnessDenominator` | Total helpfulness votes |
| `Score` | Review rating from 1 to 5 |
| `Time` | Unix timestamp of the review |
| `Summary` | Short review summary |
| `Text` | Full review text |

---

## Technologies Used

- **Apache Hadoop** — HDFS storage and MapReduce execution
- **Java** — Mapper, Reducer, and Driver implementations
- **Apache Pig** — high-level data analysis
- **Python** — dataset preprocessing and visualization
- **Matplotlib** — analytical charts and graphs
- **HDFS** — distributed input and output storage
- **Windows Command Prompt / PowerShell** — Hadoop execution environment used during the project
- **Ubuntu / WSL Bash** — final saved-output demonstration script

---

## Project Workflow

```text
Amazon Fine Food Reviews CSV
            |
            v
     Data Preprocessing
            |
            v
   Cleaned TSV Dataset
            |
            v
       Hadoop HDFS
            |
     -----------------
     |               |
     v               v
Java MapReduce    Apache Pig
  3 analyses       5 analyses
     |               |
     --------+--------
             |
             v
       Result Files
             |
             v
      Visualizations
             |
             v
        Final Report
```

---

## Project Structure

```text
BDAL-Final/
|
|-- dataset/                         # Dataset and processed/sample data
|-- jar/                             # Compiled MapReduce JAR files
|-- mapreduce/                       # Java MapReduce source code
|   |-- best-reviewer/
|   |-- product-helpfulness/
|   `-- rating-count/
|
|-- pig/                             # Apache Pig scripts
|-- preprocessing/                   # Dataset preprocessing files/scripts
|-- results/
|   |-- mapreduce/                   # Saved MapReduce results
|   `-- pig/                         # Saved Pig results
|
|-- visualization/                   # Visualization script and generated charts
|-- Amazon_Fine_Food_Reviews_Hadoop_Final_Report_Formatted.docx
|-- show_outputs.sh                  # Displays all saved final outputs
|-- .gitignore
`-- README.md
```

---

## Data Preprocessing

The preprocessing stage converts the original `Reviews.csv` dataset into a Hadoop-friendly TSV file.

### Preprocessing Summary

```text
Original records : 568,454
Valid records    : 568,452
Invalid records  : 2
Output file      : amazon_reviews.tsv
Output size      : 299,117,356 bytes
```

The preprocessing stage also creates a small sample file that can be used to inspect the cleaned format before processing the complete dataset.

---

## HDFS Storage

The cleaned dataset is uploaded to:

```text
/amazon/input/amazon_reviews.tsv
```

Example HDFS setup:

```bash
hdfs dfs -mkdir -p /amazon/input
hdfs dfs -put dataset/amazon_reviews.tsv /amazon/input/
hdfs dfs -ls -h /amazon/input
```

To inspect a small portion of the uploaded dataset:

```bash
hdfs dfs -cat /amazon/input/amazon_reviews.tsv | head
```

---

# Java MapReduce Analysis

Three Java MapReduce jobs were implemented. Each analysis contains a **Mapper, Reducer, and Driver** class and uses the cleaned TSV file stored in HDFS as input.

## 1. Best Reviewer Based on Number of Reviews

**Purpose:** Count the number of reviews submitted by each `UserId` and identify the most active reviewers.

**Map logic:**

```text
UserId -> 1
```

**Reduce logic:** Sum all values for each `UserId`.

### Top Result

| User ID | Reviews |
|---|---:|
| `A3OXHLG6DIBRW8` | 448 |
| `A1YUL9PCJR3JTY` | 421 |
| `AY12DBB0U42QB` | 389 |

The most active reviewer was **A3OXHLG6DIBRW8** with **448 reviews**.

---

## 2. Total Amazon Reviews by Rating Score

**Purpose:** Count the total number of valid reviews for rating scores 1 through 5.

**Map logic:**

```text
Score -> 1
```

**Reduce logic:** Sum all review counts for each score.

### Result

| Rating Score | Review Count |
|---:|---:|
| 1 | 52,268 |
| 2 | 29,769 |
| 3 | 42,640 |
| 4 | 80,654 |
| 5 | 363,121 |

The total is **568,452 reviews**, exactly matching the number of valid records produced during preprocessing. Rating **5** is the dominant rating with **363,121 reviews**.

---

## 3. Total Helpful Votes Based on Product ID

**Purpose:** Calculate the total helpful votes received by each product.

**Map logic:**

```text
ProductId -> HelpfulnessNumerator
```

**Reduce logic:** Sum all helpful votes for each `ProductId`.

### Top Results

| Product ID | Helpful Votes |
|---|---:|
| `B00012182G` | 3,989 |
| `B000FI4O90` | 3,535 |
| `B003B3OOPA` | 2,944 |
| `B000VK080C` | 2,630 |
| `B001LQCOIS` | 2,074 |

Product **B00012182G** received the highest total helpful-vote count with **3,989 helpful votes**.

---

# Apache Pig Analysis

Apache Pig was used for five higher-level analyses on the same cleaned HDFS dataset. The scripts use operations such as `LOAD`, `FILTER`, `GROUP`, `FOREACH`, `COUNT`, `SUM`, `ORDER`, `LIMIT`, and `STORE`.

## 1. Top 5 Products by Number of Reviews

**Script:** `top5Products.pig`

| Product ID | Review Count |
|---|---:|
| `B007JFMH8M` | 913 |
| `B0026RQTGE` | 632 |
| `B002QWP8H0` | 632 |
| `B002QWHJOU` | 632 |
| `B002QWP89S` | 632 |

Product **B007JFMH8M** had the highest number of reviews with **913 reviews**.

---

## 2. Top 10 Most Helpful Reviews

**Script:** `top10HelpfulReviews.pig`

The analysis ranks individual reviews using `HelpfulnessNumerator`.

### Top Results

| Review ID | Product ID | Score | Helpful Votes |
|---:|---|---:|---:|
| 190734 | `B000FI4O90` | 5 | 866 |
| 207713 | `B00012182G` | 3 | 844 |
| 566780 | `B001PQTYN2` | 5 | 808 |
| 235723 | `B001F10XUU` | 1 | 580 |

Review **190734** for product **B000FI4O90** ranked first with **866 helpful votes**.

---

## 3. Top 10 Helpful Reviews by Rating Score

**Script:** `top10HelpfulReviewsByScore.pig`

Reviews are grouped by rating score, and the ten most helpful reviews are selected inside each score group. The complete output contains **50 rows** — ten results for each rating score from 1 to 5.

### Leading Review for Each Score

| Score | Review ID | Product ID | Helpful Votes |
|---:|---:|---|---:|
| 1 | 235723 | `B001F10XUU` | 580 |
| 2 | 190735 | `B000FI4O90` | 524 |
| 3 | 207713 | `B00012182G` | 844 |
| 4 | 130827 | `B001CHFUDC` | 454 |
| 5 | 190734 | `B000FI4O90` | 866 |

---

## 4. Top 10 Products by Total Helpful Votes

**Script:** `top10ProductsByHelpfulVotes.pig`

This Pig analysis groups reviews by `ProductId`, sums `HelpfulnessNumerator`, sorts the products by total helpful votes, and returns the Top 10 products.

### Leading Products

| Product ID | Helpful Votes |
|---|---:|
| `B00012182G` | 3,989 |
| `B000FI4O90` | 3,535 |
| `B003B3OOPA` | 2,944 |
| `B000VK080C` | 2,630 |
| `B001LQCOIS` | 2,074 |

The leading totals match the MapReduce product-helpfulness aggregation. Some products are tied at lower positions, so tied Product IDs can differ when a secondary sort key is not defined in the same way.

---

## 5. Top 10 Products by Helpful Votes for Each Rating Score

**Script:** `top10ProductsByHelpfulVotesByScore.pig`

The analysis groups reviews using the composite key `(Score, ProductId)`, calculates helpful-vote totals, and returns the ten leading products for every rating score. The complete output contains **50 rows**.

### Leading Product for Each Score

| Score | Product ID | Helpful Votes |
|---:|---|---:|
| 1 | `B0099HD3YA` | 1,377 |
| 2 | `B000FI4O90` | 721 |
| 3 | `B00012182G` | 1,242 |
| 4 | `B001CHFUDC` | 454 |
| 5 | `B003B3OOPA` | 2,515 |

---

## Key Findings

- **Most active reviewer:** `A3OXHLG6DIBRW8` — **448 reviews**
- **Most common rating:** Score **5** — **363,121 reviews**
- **Product with highest total helpful votes:** `B00012182G` — **3,989 helpful votes**
- **Product with highest review count in Pig Top 5:** `B007JFMH8M` — **913 reviews**
- **Most helpful individual review:** Review `190734` — **866 helpful votes**
- **Total valid records processed:** **568,452**

---

## Visualizations

The project includes visualizations for the main analytical results, including:

- Top reviewers by number of reviews
- Amazon reviews by rating score
- Top products by total helpful votes using MapReduce
- Top 5 products by number of reviews using Pig
- Top 10 most helpful reviews
- Helpful reviews by rating score
- Top products by total helpful votes using Pig
- Product helpful-vote distribution by rating score

Generate the visualizations with:

```bash
python visualization/create_visualizations.py
```

Generated charts are stored inside the `visualization/` directory.

---

## Running the Project

### Prerequisites

Make sure the following are installed and configured:

- Java JDK
- Apache Hadoop
- Apache Pig
- Python 3
- Matplotlib

### 1. Clone the Repository

```bash
git clone https://github.com/Sharif1023/BDAL-Final.git
cd BDAL-Final
```

### 2. Prepare the Dataset

Download `Reviews.csv` from the Amazon Fine Food Reviews Kaggle dataset and place it in the appropriate dataset location used by the preprocessing script.

Run the preprocessing script available in the `preprocessing/` directory. After successful preprocessing, verify that `amazon_reviews.tsv` has been created.

### 3. Start Hadoop Services

On the Windows Hadoop setup used for this project:

```bat
cd C:\hadoop\sbin
start-dfs.cmd
start-yarn.cmd
jps
```

`jps` should show the required Hadoop services such as `NameNode`, `DataNode`, `ResourceManager`, and `NodeManager`.

### 4. Upload the Cleaned Dataset to HDFS

```bash
hdfs dfs -mkdir -p /amazon/input
hdfs dfs -put dataset/amazon_reviews.tsv /amazon/input/
hdfs dfs -ls -h /amazon/input
```

### 5. Run the MapReduce Jobs

The project contains the Java source code under `mapreduce/` and compiled JAR files under `jar/`.

Each Driver expects two arguments:

```text
<input HDFS path> <output HDFS path>
```

The common input path is:

```text
/amazon/input/amazon_reviews.tsv
```

Before rerunning a MapReduce job, remove its existing HDFS output directory if necessary because Hadoop does not overwrite an existing output directory.

### 6. Run the Pig Scripts

```bash
pig -x mapreduce pig/top5Products.pig
pig -x mapreduce pig/top10HelpfulReviews.pig
pig -x mapreduce pig/top10HelpfulReviewsByScore.pig
pig -x mapreduce pig/top10ProductsByHelpfulVotes.pig
pig -x mapreduce pig/top10ProductsByHelpfulVotesByScore.pig
```

Before rerunning a Pig script, remove the corresponding existing HDFS output directory if necessary.

### 7. Generate Visualizations

```bash
python visualization/create_visualizations.py
```

---

## Display All Final Saved Outputs

A helper script is included to display the saved outputs from all **3 MapReduce analyses** and **5 Pig analyses** together.

On Ubuntu / WSL:

```bash
bash show_outputs.sh
```

The script displays these result files:

```text
results/mapreduce/mr1_top10_reviewers.txt
results/mapreduce/mr2_rating_count.txt
results/mapreduce/mr3_top10_product_helpfulness.txt

results/pig/pig1_top5_products.txt
results/pig/pig2_top10_helpful_reviews.txt
results/pig/pig3_top10_helpful_by_score.txt
results/pig/pig4_top10_products_helpful.txt
results/pig/pig5_top10_products_helpful_by_score.txt
```

This is useful for quickly demonstrating all final analytical outputs without rerunning every Hadoop and Pig job.

---

## Final Report

The complete laboratory report with implementation details, execution evidence, result tables, screenshots, interpretations, and visualizations is included in the repository:

[**Amazon Fine Food Reviews Hadoop Final Report**]

Amazon_Fine_Food_Reviews_Hadoop_Final_Report.docx
Amazon_Fine_Food_Reviews_Hadoop_Final_Report.pdf

---

## Academic Information

**Course:** Big Data Analytics Lab  
**Course Code:** CSE 4346  
**Department:** Computer Science and Engineering  
**University:** Premier University Chattogram  
**Student:** Sariful Islam  
**Session:** Spring 2026

---

## References

1. Amazon Fine Food Reviews Dataset — https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
2. Apache Hadoop Documentation — https://hadoop.apache.org/
3. Apache Pig Documentation — https://pig.apache.org/
4. Reference Hadoop project — https://github.com/SiddhiPrabhu1995/YouTube-Data-Analysis-using-Hadoop

---

## Author

**Sariful Islam**  
Department of Computer Science and Engineering  
Premier University Chattogram

**GitHub Repository:** https://github.com/Sharif1023/BDAL-Final
