'''CLEANING THE TEXT BY REMOVING STOPWORDS'''

stopwords_file = r"C:\Users\Rohith\Desktop\intership\StopWords\ALL STOPWORDS .txt"# READING the combination all stopwords files
with open(stopwords_file, 'r', encoding='utf-8') as file:
    stopwords = set(file.read().split())# opening the file of stowords  
text_file = r"C:\Users\Rohith\Desktop\intership\extracted txt\blackassign0001.txt"# READING the first text file from Artical
with open(text_file, 'r', encoding='utf-8') as file:
    text = file.read()
cleaned_text = ' '.join(word for word in text.split() if word.lower() not in stopwords)# condition to remove stopwords from the text file
print("Cleaned Text:")
print(cleaned_text)
print('\n')
#**********************************************************************************************************************************************************************************


'''CREATING A DICTIONARY OF POSITIVIE AND NEGITIVE WORDS'''

positive_words = {}
negative_words = {}
with open(r"C:\Users\Rohith\Desktop\intership\MasterDictionary\positive-words.txt", 'r') as file:
    for line in file:# reading the positive words text file
        word = line.strip().lower()
        if word not in stopwords:
            positive_words[word] = 1
with open(r"C:\Users\Rohith\Desktop\intership\MasterDictionary\negative-words.txt", 'r') as file:
    for line in file:# reading the negative words text file
        word = line.strip().lower()
        if word not in stopwords:
            negative_words[word] = -1
#we add only those words in the dictionary if they are not found in the Stop Words Lists. 

print("First 4 Positive Words =",dict(list(positive_words.items())[:4]))
print("First 4 Negative Words =",dict(list(negative_words.items())[:4]))
print('\n')
print('Number of positive words=',len(positive_words))
print('Number of negative words=',len(negative_words))
print('\n')
#***************************************************************************************************************************************************************************************

'''EXTRACTING DERIVED VARIABLES'''

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

tokens = word_tokenize(cleaned_text.lower())
positive_score = 0
negative_score = 0
total_words = len(tokens)

# Calculate Positive Score and Negative Score
for word in tokens:
    if word in positive_words:
        positive_score += 1#                                                                      1
    elif word in negative_words:
        negative_score += 1#......................................................................2

# Calculate Polarity Score
polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)#3

# Calculate Subjectivity Score
subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)#................4 

# Print the calculated scores
print("1.Positive Score:", positive_score)
print("2.Negative Score:", negative_score)
print("3.Polarity Score:", round(polarity_score,2))
print("4.Subjectivity Score:", round(subjectivity_score,2))

#**********************************************************************************************************************************************************************************
''' ANALYSIS OF READABILITY '''

sentences = sent_tokenize(cleaned_text)
words = word_tokenize(cleaned_text.lower())
average_sentence_length = len(words) / len(sentences)#............................................5
print("5.Average Sentence Length:", round(average_sentence_length,2))
#*************************************************************************************************************************************************************************************
'''Complex Word Count'''

# Define a list of complex words (replace this with your actual list of complex words)
complex_words = ["proportion", "combination"]
# Calculate Percentage of Complex Words
complex_word_count = sum(1 for word in words if word in complex_words)#...........................6
print("6.Complex Word Count:", complex_word_count)
#**********************************************************************************************************************************************************************************
percentage_complex_words = complex_word_count / len(words)#.......................................7
print("7.Percentage of Complex Words:", percentage_complex_words)
#***********************************************************************************************************************************************************************************

# Calculate Fog Index
fog_index = 0.4 * (average_sentence_length + percentage_complex_words)#...........................8
print("8.Fog Index:", round(fog_index,2))
#**********************************************************************************************************************************************************************************

'''Word Count'''
# Calculate Average Number of Words Per Sentence
total_words=len(words)#...........................................................................9
print("9.Word Count:", total_words)
#************************************************************************************************************************************************************************************

'''Average Number of Words Per Sentence'''
total_sentences=len(sentences)
average_words_per_sentence = total_words / total_sentences#.......................................10
print("10.Average Number of Words Per Sentence:", round(average_words_per_sentence,2))
#*************************************************************************************************************************************************************************************

'''Average Word Length'''
average_word_length = sum(len(word) for word in words) / total_words#.............................11
print("11.Average Word Length:", round(average_word_length,2))
#*************************************************************************************************************************************************************************************


'''Syllable Count Per Word'''
# Count syllables for each word
syllable_count = sum(1 for word in words for char in word if char in "aeiouy")#...................12
print("12.Total Syllable Count:", syllable_count)
#*************************************************************************************************************************************************************************************

'''Personal Pronouns'''
# Define a regex pattern for personal pronouns
personal_pronoun_pattern = r'\b(I|we|my|ours|us)\b'
personal_pronoun_count = 0
import re
# Count personal pronouns in the text using regex
for word in words:
    if re.match(personal_pronoun_pattern, word):
        personal_pronoun_count += 1#..............................................................13
print("13.Personal Pronoun Count:", personal_pronoun_count)

#******************************************************************************************************************************************************************************************

import pandas as pd
data = {
    "Metric": ["Positive Score", "Negative Score", "Polarity Score", "Subjectivity Score",
               "Average Sentence Length", "Complex Word Count", "Percentage of Complex Words",
               "Fog Index", "Word Count", "Average Number of Words Per Sentence",
               "Average Word Length", "Total Syllable Count", "Personal Pronoun Count"],
    "Value": [positive_score, negative_score, round(polarity_score, 2), round(subjectivity_score, 2),
              round(average_sentence_length, 2), complex_word_count, round(percentage_complex_words, 2),
              round(fog_index, 2), total_words, round(average_words_per_sentence, 2),
              round(average_word_length, 2), syllable_count, personal_pronoun_count]}
df = pd.DataFrame(data)
df_transposed = df.transpose()# changeing the row values into columns
excel_file = r"C:\Users\Rohith\Downloads\Input.xlsx"
df_transposed.to_excel(excel_file, index=False, header=False)
print("Output saved to:", excel_file)








