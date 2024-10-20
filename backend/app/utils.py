import arxiv
import pdfplumber
import requests
import os


def fetch_paper_text(arxiv_id: str) -> str:
    try:
        # Search for the paper by arXiv ID
        search = arxiv.Search(id_list=[arxiv_id])
        paper = next(search.results())

        # Get the abstract as a fallback
        abstract = paper.summary

        # Download the PDF if available
        pdf_url = paper.pdf_url
        pdf_path = f"/tmp/{arxiv_id}.pdf"

        # Download the PDF
        response = requests.get(pdf_url)
        with open(pdf_path, "wb") as f:
            f.write(response.content)

        # Extract text from the PDF using pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text()

        # Remove the temporary PDF file
        os.remove(pdf_path)

        return full_text or abstract  # Return the full text if available, otherwise fallback to the abstract
    except Exception as e:
        raise Exception(f"Error fetching paper from arXiv: {str(e)}")
