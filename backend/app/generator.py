import openai
from .config import OPENAI_API_KEY

# Initialize OpenAI with the API key
openai.api_key = OPENAI_API_KEY

def generate_research_directions(prompt: str):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Specify the engine/model
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Extract the generated text from the response
    return response.choices[0].text.strip()
