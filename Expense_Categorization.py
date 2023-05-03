import sys
import pandas as pd
import spacy
from collections import Counter

# Check if a file name was provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script_name.py <Excel_file_path>")
    sys.exit(1)

# Configuration
file_path = sys.argv[1]  # Get the file path from the command-line argument
sheet_name = "Accounting"  # Name of the sheet containing your transactions
description_column = "Name"  # Name of the column with transaction descriptions

# Read data from the Excel file
data = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")

# Combine all transaction descriptions into a single text
all_descriptions = " ".join(data[description_column])

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Process the combined transaction descriptions text
doc = nlp(all_descriptions)

# Extract tokens that are not stopwords or punctuation
meaningful_words = [token.text for token in doc if not token.is_stop and not token.is_punct]

# Count the frequency of each unique word
meaningful_word_counts = Counter(meaningful_words)

# Sort the words by frequency in descending order
sorted_meaningful_word_counts = sorted(meaningful_word_counts.items(), key=lambda x: x[1], reverse=True)

# Print the sorted list of meaningful keywords and their frequencies

print(sorted_meaningful_word_counts)

# Process each transaction description separately and store row numbers along with keyword count
word_occurrences = {}

for index, row in data.iterrows():
    description = row[description_column]
    doc = nlp(description)

    meaningful_words = [token.text for token in doc if not token.is_stop and not token.is_punct]

    for word in meaningful_words:
        if word not in word_occurrences:
            word_occurrences[word] = []

        word_occurrences[word].append(index + 1)  # Add 1 to the index to match Excel's 1-based row numbering

# Print the sorted list of meaningful keywords, their frequencies, and row numbers where they occur
for word, count in sorted_meaningful_word_counts:
    print(f"{word}: {count}, Rows: {word_occurrences[word]}")
