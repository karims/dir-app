from fastapi import FastAPI, HTTPException

from .summarizer import summarize_and_generate
from .database import save_summary_to_db

app = FastAPI()

@app.post("/process/")
def process_research_paper(arxiv_id: str):
    try:
        summary, research_directions = summarize_and_generate(arxiv_id)
        # Store the results in MongoDB
        save_summary_to_db(arxiv_id, summary, research_directions)
        return {"summary": summary, "research_directions": research_directions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
