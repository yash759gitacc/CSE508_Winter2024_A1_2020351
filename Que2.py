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



# Step 2: Save and load inverted index
def save_inverted_index(inverted_index, output_path):
    with open(output_path, 'wb') as file:
        pickle.dump(inverted_index, file)

def load_inverted_index(input_path):
    with open(input_path, 'rb') as file:
        inverted_index = pickle.load(file)
    return inverted_index







def tokenize(text):
    return Que1_1.preprocess_text(text)

def get_set_ofAll_files(invertedIndex):
    ans = set()
    for token in inverted_index:
        temp = set(inverted_index[token])
        ans = ans.union(temp)
    return ans

def perform_and_query(term1_docs, term2_docs):
    return term1_docs.intersection(term2_docs)

def perform_or_query(term1_docs, term2_docs):
    return term1_docs.union(term2_docs)

def perform_not(text , inverted_index):
    allDocs = set(get_set_ofAll_files())
    temp = set(inverted_index[text])
    return allDocs.remove(temp)


def askQuery(text , query , inverted_index):
    docs = []
    tokens = tokenize(text)
    print(tokens)
    for i in range(len(tokens)):
        token = tokens[i]
        docs.append( set(inverted_index[token]) )
        print(token ,end=" ")
        if (i<len(query)):
            print(query[i] , end=" ")
        else:
            print()

    for i in range(len(query)):
        temp = query[i]
        if temp[-3:] == "NOT":
            query[i] = temp[:-3].strip()
            docs[i+1] = perform_not(tokens[i+1],inverted_index)

    docs2 = []
    for i in range(len(query)):
        if query[i] == "OR":
            docs.append(docs[i])
        if query[i] == "AND":
            temp = perform_and_query( docs[i] , docs[i+1])
            docs[i+1] = temp
    docs2.append(docs[-1])

    ans = set()
    for temp in docs2:
        ans = perform_or_query(ans,temp)
    return ans




#Starting the program
dataset_dir = "preprocessed_dataset"
inverted_index = create_inverted_index("output")
save_inverted_index(inverted_index, "inverted_index.pickle")
inverted_index = load_inverted_index("inverted_index.pickle")

# taking input and printing Output
print(" Enter Input")
for  i in range( int(input("Enter no. of queries")) ):
    text = input("Enter Input sequence: ")
    operations = input("Enter Operations separated by comma: ")
    operations = [x.strip() for x in operations.split(',')]
    result = askQuery(text, operations,inverted_index)
    print("No of files: ",len(result))
    print("name of files: ",result)




