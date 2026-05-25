import openai
from typing import List

class SummaryAgent:
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)

    def generate_summary(self, chunks: List[str]) -> str:
        """
        Generate a context-aware summary from document chunks.
        """
        context = "\n".join(chunks)
        prompt = f"""
        You are a summary agent. Your task is to generate a concise, faithful summary of the following document.
        Preserve intent, decisions, constraints, and assumptions.

        Document:
        {context}

        Summary:
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
