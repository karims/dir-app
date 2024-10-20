from pymongo import MongoClient
from config import MONGO_URI


client = MongoClient(MONGO_URI)
db = client['rag_db']

def save_summary_to_db(arxiv_id, summary, research_directions):
    collection = db['summaries']
    document = {
        "arxiv_id": arxiv_id,
        "summary": summary,
        "research_directions": research_directions
    }
    collection.insert_one(document)
