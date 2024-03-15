import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read the Excel file containing URLs
df = pd.read_excel(r'C:\Users\Rohith\Downloads\Input.xlsx')

# Function to extract article title and text from a URL
def extract_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.get_text() if soup.title else ""
        text = '\n'.join([p.get_text() for p in soup.find_all('p')])
        return title, text
    else:
        return "", ""

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    url_id, url = row['URL_ID'], row['URL']
    title, text = extract_article(url)
    if text:
        with open(f"{url_id}.txt", 'w', encoding='utf-8') as f:
            f.write(f"Title: {title}\n\n{text}")
        print(f"Extracted article from {url} and saved to {url_id}.txt")
    else:
        print(f"Failed to fetch {url}")

print("Extraction complete.")

'''1.EXPLAINING HOW YOU APPROACHED THE SOLUTION?
A.There are mainly 3 steps to do the text analysis 
Step 1:
Reading the data(100 txt files):
Define the paths to text files and the stopwords file,Read stopwords from the stopwords file into a set,and Read positive and negative words from separate files into dictionaries.

Step 2: 
Iterate over each text file(100 txt files) in the folder:
Actually i have done text analysis for the 1 text file later I took help from ai tools like chatgpt to iterate over the folder of 100 text files.
Tokenize the text into words and sentences using NLTK from NLP.
Calculate various metrics such as 
1.positive score
2. negative score
3.polarity score 
4.subjectivity score,
5.average sentence length 
6.complex word count 
7.percentage of complex words
8.fog index
9.word count
10.average number of words per sentence
11.average word length
12.total syllable count
13.personal pronoun count.
And Store the calculated metrics in a dictionary to save the values for 100 text files in excel

Step 3: 
Saveing the Data into excel file:
Convert the list of dictionaries containing metrics into a pandas DataFrame.  Save the DataFrame to an Excel file.


2. How to run the .py file to generate output?
A . Save the Python code provided in a .py file (TEXT ANALYSIS FOR ALL ARTICLE’S TEXT.py), Make sure u have the package like pandas, nltk, regx, beautifulsoap4, and requests if not use pip install and Run the script .
The script will process the text files, calculate metrics, and save the results to an Excel file.


DATA EXTRACTION FROM URLS
1. imports necessary libraries (pandas, requests, BeautifulSoup) to handle data manipulation, HTTP requests, and HTML parsing. It reads the input data from an Excel file using pd.read_excel() and stores it in a pandas DataFrame.
2.Extracting Articles:
It defines a function extract_article() to extract the article title and text from a given URL. Inside this function, it makes an HTTP request to the URL using requests.get() to retrieve the HTML content.
It then parses the HTML content using BeautifulSoup to extract the title and text of the article.

3.Iterating Over URLs:
The script iterates over each row in the DataFrame using df.iterrows(). For each row, it extracts the URL and calls the extract_article() function to fetch the title and text of the article.
If the text is successfully extracted, it saves the title and text to a text file named after the URL ID.

4.Saving Output AS as same file name:
The extracted text is saved to individual text files with the format "Title: [title]\n\n[text]".
A completion message is printed after the extraction process is finished.



NOTE: text analysis for the extracted data is familiar to me, Thanks to the project I have done on the text summerization using nltk and spacy , which u can find it in my resume or in my githup repository.
But data extraction from articles comes under the webscraping or Data crawling where im poor at but I took the help of ai tools to get perfect code to extract the data from 100 articals by iterating 100 urls by using pandas librerie. By the way im strong at data analysis[eda], data visualization [powerbi,dax,Tableau]  and machine learnig and nlp. Which u can find the projects of them in my           github:-
https://github.com/RohithBatcha



THANK YOU'''

