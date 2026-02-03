def retrieve(vector_store, query_embedding, top_k):
    return vector_store.search(query_embedding, top_k)
