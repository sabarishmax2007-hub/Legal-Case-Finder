from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from vector_store import search
from reranker import rerank

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Legal Case Finder Running 🚀"}

@app.get("/search")
def search_cases(query: str):
    results = search(query)
    ranked_results = rerank(query, results)

    return {
        "query": query,
        "results": ranked_results
    }