from haystack.pipelines import Pipeline
from haystack.nodes import TransformersSummarizer
from generator import generate_research_directions
from utils import fetch_paper_text


def summarize_and_generate(arxiv_id: str):
    # Fetch the paper text from arXiv
    paper_text = fetch_paper_text(arxiv_id)

    # Initialize Haystack summarizer
    summarizer = TransformersSummarizer(model_name_or_path="facebook/bart-large-cnn")

    # Run summarization
    summary_output = summarizer.predict(paper_text)
    summary = summary_output['summary_text']

    # Create the prompt for generating research directions
    prompt_template = f"""
    The research paper you summarized discusses the problem of {summary}.

    Based on this, what are some potential future research directions, improvements, or unresolved challenges that researchers should focus on next?
    """

    # Generate research directions using OpenAI's GPT
    research_directions = generate_research_directions(prompt_template)

    return summary, research_directions
