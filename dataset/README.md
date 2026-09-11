\# Amazon Fine Food Reviews Dataset



\## Dataset Source



The dataset used in this project is the \*\*Amazon Fine Food Reviews\*\* dataset available on Kaggle.



Dataset link:



https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews



\## Dataset Description



The original dataset contains Amazon fine food product reviews and includes the following attributes:



| Field | Description |

|---|---|

| Id | Unique review identifier |

| ProductId | Amazon product identifier |

| UserId | Unique reviewer identifier |

| ProfileName | Reviewer profile name |

| HelpfulnessNumerator | Number of users who found the review helpful |

| HelpfulnessDenominator | Total helpfulness votes |

| Score | Product rating from 1 to 5 |

| Time | Review timestamp |

| Summary | Review summary |

| Text | Full review text |



\## Dataset Preprocessing



The original CSV file was converted into a tab-separated dataset for reliable Hadoop and Apache Pig processing.



Preprocessing statistics:



\- Total CSV records: 568,454

\- Valid records: 568,452

\- Invalid records: 2

\- Cleaned dataset file: `amazon\_reviews.tsv`

\- Cleaned dataset size: 299,117,356 bytes



Tabs, newline characters and carriage returns inside text fields were cleaned to make the dataset suitable for Hadoop processing.



\## Large Dataset Files



The following files are intentionally not included in this GitHub repository because of their size:



\- `Reviews.csv`

\- `Reviews.csv.zip`

\- `amazon\_reviews.tsv`



A small sample is included as:



`sample\_amazon\_reviews.tsv`



Users can download the full dataset from Kaggle and run:



```bash

python preprocessing/prepare\_dataset.py

