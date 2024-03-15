import os
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
import re

folder_path = r"C:\Users\Rohith\Desktop\intership\extracted txt"

stopwords_file = r"C:\Users\Rohith\Desktop\intership\StopWords\ALL STOPWORDS .txt"
with open(stopwords_file, 'r', encoding='utf-8') as file:
    stopwords = set(file.read().split())

positive_words = {}
negative_words = {}
with open(r"C:\Users\Rohith\Desktop\intership\MasterDictionary\positive-words.txt", 'r') as file:
    for line in file:
        word = line.strip().lower()
        if word not in stopwords:
            positive_words[word] = 1
with open(r"C:\Users\Rohith\Desktop\intership\MasterDictionary\negative-words.txt", 'r') as file:
    for line in file:
        word = line.strip().lower()
        if word not in stopwords:
            negative_words[word] = -1

# Define a list of complex words (replace this with your actual list of complex words)
complex_words = ["proportion", "combination"]

# List to store metrics for each text file
metrics_list = []

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            tokens = word_tokenize(text.lower())
            sentences = sent_tokenize(text)
            words = word_tokenize(text.lower())
            total_words = len(words)
            
            positive_score = sum(1 for word in tokens if word in positive_words)
            negative_score = sum(1 for word in tokens if word in negative_words)
            
            polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
            subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)
            
            average_sentence_length = len(words) / len(sentences)
            complex_word_count = sum(1 for word in words if word in complex_words)
            percentage_complex_words = complex_word_count / len(words)
            
            fog_index = 0.4 * (average_sentence_length + percentage_complex_words)
            total_syllable_count = sum(1 for word in words for char in word if char in "aeiouy")
            
            personal_pronoun_pattern = r'\b(I|we|my|ours|us)\b'
            personal_pronoun_count = sum(1 for word in words if re.match(personal_pronoun_pattern, word))
            
            average_word_length = sum(len(word) for word in words) / total_words
            
            metrics = {
                "File Name": filename,
                "Positive Score": positive_score,
                "Negative Score": negative_score,
                "Polarity Score": round(polarity_score, 2),
                "Subjectivity Score": round(subjectivity_score, 2),
                "Average Sentence Length": round(average_sentence_length, 2),
                "Complex Word Count": complex_word_count,
                "Percentage of Complex Words": round(percentage_complex_words, 2),
                "Fog Index": round(fog_index, 2),
                "Word Count": total_words,
                "Average Number of Words Per Sentence": round(average_sentence_length, 2),
                "Average Word Length": round(average_word_length, 2),
                "Total Syllable Count": total_syllable_count,
                "Personal Pronoun Count": personal_pronoun_count
            }
            metrics_list.append(metrics)


df = pd.DataFrame(metrics_list)

excel_file = r"C:\Users\Rohith\Desktop\exp.xlsx"
df.to_excel(excel_file, index=False)
print("Output saved to:", excel_file)
