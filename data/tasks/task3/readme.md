# Sentiment and Issue Classification for Product Reviews

This Python script processes customer reviews from a CSV file, performs sentiment analysis, and classifies the type of issue (product, delivery, service, or general) mentioned in each review. The results are saved in a new CSV file with additional columns for sentiment and issue type.

## Requirements

Before running the script, make sure to have the following Python packages installed:

- `pandas` - For data manipulation and CSV file handling.
- `textblob` - For sentiment analysis.
- `re` - For regular expressions used in issue classification.

You can install the required libraries using `pip`:

```bash
pip install pandas textblob
