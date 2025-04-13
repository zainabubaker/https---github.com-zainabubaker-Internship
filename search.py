import json
import torch
from sklearn.metrics.pairwise import cosine_similarity
from combined_script import get_tokenizer_and_model
import arabic_reshaper
from bidi.algorithm import get_display

tokenizer, model = get_tokenizer_and_model()

def preprocess_query(query):
    reshaped_query = arabic_reshaper.reshape(query)
    bidi_query = get_display(reshaped_query)
    return bidi_query

def search(query, embeddings_dict, top_n=5):
    preprocessed_query = preprocess_query(query)
    query_input = tokenizer(preprocessed_query, return_tensors='pt', padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        query_output = model(**query_input)
        query_embedding = query_output.last_hidden_state.mean(dim=1)

    similarities = {}
    for file, embedding in embeddings_dict.items():
        sim = cosine_similarity(query_embedding, torch.tensor(embedding).unsqueeze(0))
        similarities[file] = sim.item()

    sorted_results = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
    return sorted_results[:top_n]

def load_embeddings(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == '__main__':
    embeddings_dict = load_embeddings('embeddings.json')
    query = "SSE Family Intrinsics"
    results = search(query, embeddings_dict)
    print("Top results:", results)