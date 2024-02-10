import os
import pickle
import Que1_1

# Load positional index
def load_positional_index(input_path):
    with open(input_path, 'rb') as file:
        positional_index = pickle.load(file)
    return positional_index

def tokenize(text):
    return Que1_1.preprocess_text(text)

# Function to find files containing a phrase query
def find_files_with_phrase(positional_index, phrase_query):
    query_terms = tokenize(phrase_query)
    print(query_terms)
    files_containing_phrase = set()
    if len(query_terms) < 2:
        return files_containing_phrase
    # Get the positions of the first term
    first_term = query_terms[0]
    if first_term in positional_index:
        for file_name, positions in positional_index[first_term].items():
            for position in positions:
                # Check if the other terms in the phrase query occur consecutively
                all_terms_found = True
                for i in range(1, len(query_terms)):
                    if file_name not in positional_index.get(query_terms[i], {}) or position + i not in positional_index[query_terms[i]][file_name]:
                        all_terms_found = False
                        break
                if all_terms_found:
                    files_containing_phrase.add(file_name)
    return files_containing_phrase


# Load pickle file
positional_index = load_positional_index("positional_index.pickle")

# take user input and print output
for i in range(int(input("Enter no of queries: "))):
    temp = "Enter phrase query "+str(i)+" : "
    phrase_query = input(temp)
    files_with_phrase = find_files_with_phrase(positional_index, phrase_query)
    print("Number of documents retrieved for query "+str(i)+" using positional index:",len(files_with_phrase))
    print("Names of documents retrieved for query "+str(i)+" using positional index:", files_with_phrase)
