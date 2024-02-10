import os
import string
import nltk
from nltk.corpus import stopwords

# Step 1: Read contents of the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Step 2: Lowercase the text
def lowercase_text(text):
    return text.lower()

# Step 3: Tokenization
def tokenize_text(text):
    return nltk.word_tokenize(text)


# Step 4: Remove stopwords
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

# Step 5: Remove punctuations
def remove_punctuations(tokens):
    # return text.translate(str.maketrans('', '', string.punctuation))
    return [token for token in tokens if token not in string.punctuation]

# Step 6: Remove blank space tokens
def remove_blank_spaces(tokens):
    return [token for token in tokens if token.strip()]


def save_preprocessed_text(tokens, output_path):
    directory = os.path.dirname(output_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(output_path, 'w') as file:
        file.write(' '.join(tokens))


# Preprocessing pipeline
def preprocess_file(input_file, output_file):
    text = read_file(input_file)
    text = lowercase_text(text)
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = remove_punctuations(tokens)
    tokens = remove_blank_spaces(tokens)
    save_preprocessed_text(tokens, output_file)


def preprocess_text(text):
    text = lowercase_text(text)
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = remove_punctuations(tokens)
    tokens = remove_blank_spaces(tokens)
    return tokens


for i in range(999):
    preprocess_file("text_files/file"+ str(i+1)+".txt","output/file"+str(i+1)+".txt" )
