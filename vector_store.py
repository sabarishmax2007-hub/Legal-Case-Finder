import faiss
import numpy as np
import json
from embedding import get_embedding

# Load cases
with open('data/cases.json', 'r') as f:
    cases = json.load(f)

texts = [case["text"] for case in cases]

# Convert to embeddings
embeddings = np.array([get_embedding(text) for text in texts]).astype('float32')

# FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def search(query, k=5):
    query_vector = np.array([get_embedding(query)]).astype('float32')
    distances, indices = index.search(query_vector, k)

    results = []
    for idx in indices[0]:
        results.append(cases[idx])

    return results