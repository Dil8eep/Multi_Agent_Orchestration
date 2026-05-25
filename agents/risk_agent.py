import openai
from typing import List

class RiskAgent:
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)

    def identify_risks(self, context: str, summary: str, actions: List[dict]) -> List[str]:
        """
        Identify risks, open issues, and assumptions from document context, summary, and actions.
        """
        actions_str = "\n".join([f"- {action['task']}" for action in actions])
        prompt = f"""
        You are a risk analysis agent. Based on the document summary, context, and extracted actions, identify:
        - Missing information
        - Open questions
        - Assumptions
        - Execution risks

        Summary:
        {summary}

        Context:
        {context}

        Actions:
        {actions_str}

        Output as a list of strings.
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.3
        )
        content = response.choices[0].message.content.strip()
        # Parse the list
        risks = [line.strip('- ').strip() for line in content.split('\n') if line.strip()]
        return risks
