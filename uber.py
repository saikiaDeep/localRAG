from sklearn.metrics.pairwise import cosine_similarity
from helpers.embeddings import create_bge_embeddings
import os
import pickle
import numpy as np

def search(query, top_k, vectors, chunks):
   
    query_vector = create_bge_embeddings([query])[0]
    query_vector = np.array(query_vector).reshape(1, -1)
    vectors = np.array(vectors)
    
    similarities = cosine_similarity(query_vector, vectors)[0]
    indexed_similarities = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)
 
    results = [chunks[i] for i, _ in indexed_similarities[:top_k]]
        
    
    return results

def load_embeddings():
    file_path = 'pkl/embeddings.pkl'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'The file {file_path} does not exist.')
    with open(file_path, 'rb') as file:
        embeddings = pickle.load(file)
    print(f'Embeddings loaded from {file_path}')
    return embeddings

# Load embeddings and chunks
embeddings_data = load_embeddings()
vectors = embeddings_data['embeddings']
chunks = embeddings_data['chunks']  # Assuming chunks are stored in the same file

# Perform search
query = "your query here"
top_k = 10
print(search(query, top_k, vectors, chunks))


