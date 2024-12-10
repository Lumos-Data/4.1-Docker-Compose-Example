import requests
from sentence_transformers import SentenceTransformer

# Qdrant API URL
QDRANT_URL = "http://localhost:6333"

# Initializing SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Preprocessing text by splitting into sentences
def preprocess_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    sentences = text.split('.')
    return [sentence.strip() for sentence in sentences if sentence.strip()]

# Recreating the Qdrant collection
def recreate_collection(collection_name):
    print(f"Deleting collection '{collection_name}'...")
    requests.delete(f"{QDRANT_URL}/collections/{collection_name}")
    print(f"Creating collection '{collection_name}'...")
    response = requests.put(
        f"{QDRANT_URL}/collections/{collection_name}",
        json={
            "vectors": {
                "size": 384,  
                "distance": "Cosine"
            }
        }
    )
    return response.json()


def insert_vectors(collection_name, texts):
    vectors = model.encode(texts).tolist()  
    points = [
        {"id": i, "vector": vectors[i], "payload": {"text": texts[i]}}
        for i in range(len(texts))
    ]
    response = requests.put(
        f"{QDRANT_URL}/collections/{collection_name}/points",
        json={"points": points}
    )
    return response.json()


def query_qdrant(collection_name, query):
    query_vector = model.encode([query]).tolist()[0] 
    response = requests.post(
        f"{QDRANT_URL}/collections/{collection_name}/points/search",
        json={
            "vector": query_vector,
            "top": 1, 
            "with_payload": True  
        }
    )
    return response.json()

# Main script
if __name__ == "__main__":
    file_path = "snowwhite.txt"  
    collection_name = "snowwhite_collection"
    query = "Mirror, mirror, on the wall, who in this land is fairest of all?"

    # 1. Recreate the collection
    print(recreate_collection(collection_name))

    # 2. Load and preprocess the text
    print("Loading text from file...")
    sentences = preprocess_text(file_path)
    print(f"Processed {len(sentences)} sentences.")

    # 3. Insert vectors into Qdrant
    print("Inserting data into Qdrant collection...")
    print(insert_vectors(collection_name, sentences))

    # 4. Query the collection
    print(f"Querying Qdrant for: \"{query}\"")
    result = query_qdrant(collection_name, query)

    # 5. Display the result
    print("\nQuery Result:")
    if "result" in result and result["result"]:
        # Retrieve the single best result
        best_match = result["result"][0]
        payload = best_match.get("payload", {})
        text = payload.get("text", "No text available")
        score = best_match.get("score", 0)
        print(f"Best Match: \"{text}\"\nRelevance Score: {score:.4f}")
    else:
        print(f"No result found for the query: \"{query}\"")
