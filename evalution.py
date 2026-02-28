import requests

API_URL = "http://127.0.0.1:8000/query"

test_queries = [
    "What is ETL?",
    "What does the API require?",
    "Explain system architecture",
]

for query in test_queries:
    response = requests.post(API_URL, json={"query": query})
    print("\nQuery:", query)
    print("Response:", response.json())