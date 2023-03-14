# Import necessary packages
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os

os.environ['OPENAI_API_KEY'] = 'sk-' #enter OpenAI API

# Loading from a directory
documents = SimpleDirectoryReader('data').load_data()

# Construct a simple vector index
index = GPTSimpleVectorIndex(documents)

# Save your index to a index.json file
index.save_to_disk('index.json')
# Load the index from your saved index.json file
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# Define the chatbot function
def chatbot():
    while True:
        user_input = input("User: ")
        response = index.query(user_input)
        print(response)

# Run the chatbot function
chatbot()
