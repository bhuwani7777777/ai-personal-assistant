# tasks/info.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def answer_question(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=100
    )
    return response.choices[0].text.strip()
