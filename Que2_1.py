import os
import string
import pickle
import Que1_1

# Step 1: Create unigram inverted index
def create_inverted_index(dataset_dir):
    inverted_index = {}
    for file_name in os.listdir(dataset_dir):
        file_path = os.path.join(dataset_dir, file_name)
        with open(file_path, 'r') as file:
            text = file.read()
            tokens = text.split()
            for token in tokens:
                if token not in inverted_index:
                    inverted_index[token] = set()
                inverted_index[token].add(file_name)
    return inverted_index



# Save inverted index
def save_inverted_index(inverted_index, output_path):
    with open(output_path, 'wb') as file:
        pickle.dump(inverted_index, file)


#Starting the program
dataset_dir = "preprocessed_dataset"
inverted_index = create_inverted_index("output")
save_inverted_index(inverted_index, "inverted_index.pickle")