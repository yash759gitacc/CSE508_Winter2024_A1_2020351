import os
import string
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords

# Step 1: Read contents of the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


# Preprocessing pipeline
def showText(input_file, output_file):

    text = read_file(input_file)
    text2 = read_file(output_file)

    print("Original text from", input_file, ":\n", text,end="\n")
    print("Processed text from", output_file, ":\n" , text2 , end="\n\n")



for i in range(5):
    showText("text_files/file"+ str(i+1)+".txt","output/file"+str(i+1)+".txt" )
