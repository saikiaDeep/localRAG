from sklearn.metrics.pairwise import cosine_similarity
from helpers.embeddings import create_bge_embeddings
import os
import pickle
import numpy as np

class QueryEngine:
    def __init__(self):
        embeddings_data = self.load_embeddings()
        self.embeddings = embeddings_data['embeddings']
        self.chunks = embeddings_data['chunks']
    def search(self,query,top_k = 10):

        query_vector = create_bge_embeddings([query])[0]
        query_vector = np.array(query_vector).reshape(1, -1)
        vectors = np.array(self.embeddings)

        similarities = cosine_similarity(query_vector, vectors)[0]
        indexed_similarities = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)
        results = [self.chunks[i] for i, _ in indexed_similarities[:top_k]]
        return results  

    def load_embeddings(self):
        file_path = 'pkl/embeddings.pkl'
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'The file {file_path} does not exist.')
        with open(file_path, 'rb') as file:
            embeddings = pickle.load(file)
        print(f'Embeddings loaded from {file_path}')
        return embeddings    
    def process_response(self,query):
        results = self.search(query)
        





    
