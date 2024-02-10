import os
import pickle
import Que1_1

# Step 1: Read contents of the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def tokenize(text):
    return Que1_1.preprocess_text(text)


# Step 3: Create positional index
def create_positional_index(dataset_dir):
    positional_index = {}
    for file_name in os.listdir(dataset_dir):
        file_path = os.path.join(dataset_dir, file_name)
        text = read_file(file_path)
        tokens = tokenize(text)
        for position, token in enumerate(tokens):
            if token not in positional_index:
                positional_index[token] = {}
            if file_name not in positional_index[token]:
                positional_index[token][file_name] = []
            positional_index[token][file_name].append(position)
    return positional_index





# Step 4: Save positional index using pickle
def save_positional_index(positional_index, output_path):
    with open(output_path, 'wb') as file:
        pickle.dump(positional_index, file)

# Step 5: Load positional index using pickle
def load_positional_index(input_path):
    with open(input_path, 'rb') as file:
        positional_index = pickle.load(file)
    return positional_index


# Sample test case
dataset_dir = "text_files"
positional_index = create_positional_index(dataset_dir)
save_positional_index(positional_index, "positional_index.pickle")

# Load positional index
loaded_positional_index = load_positional_index("positional_index.pickle")
