from sklearn.metrics.pairwise import cosine_similarity
from helpers.embeddings import create_bge_embeddings

def search(query = "Hello",top_k = 10):
    similarities = cosine_similarity([query_vector], vectors)[0]
    indexed_similarities = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)
    results = []
    for i, similarity in indexed_similarities[:top_k]:
        result = {
            'chunk': chunks[i],
            'similarity': similarity,
        }
        results.append(result)
    query_vector = create_bge_embeddings([query])[0]
