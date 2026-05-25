import openai
from typing import List
import json

class ActionAgent:
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)

    def extract_actions(self, context: str, summary: str) -> List[dict]:
        """
        Extract actionable tasks with dependencies from document context and summary.
        """
        prompt = f"""
        You are an action extraction agent. Based on the document summary and context, extract actionable tasks.
        For each task, identify owner (if available), dependencies, and deadline (if available).

        Summary:
        {summary}

        Context:
        {context}

        Output as a JSON list of objects with keys: task, owner, dependencies, deadline.
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.3
        )
        content = response.choices[0].message.content.strip()
        try:
            actions = json.loads(content)
            return actions
        except json.JSONDecodeError:
            # Fallback: parse manually or return empty list
            return []
