from typing import List, Dict
from agents.summary_agent import SummaryAgent
from agents.action_agent import ActionAgent
from agents.risk_agent import RiskAgent
from utils.vector_db import VectorDB
from utils.preprocessing import clean_text, chunk_document

class Orchestrator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.summary_agent = SummaryAgent(api_key)
        self.action_agent = ActionAgent(api_key)
        self.risk_agent = RiskAgent(api_key)
        self.vector_db = VectorDB(api_key)

    def process_document(self, document: str) -> Dict:
        # Step 1: Preprocess document
        doc = clean_text(document)
        chunks = chunk_document(doc)

        # Step 2: Create vector memory
        self.vector_db.create_vectorstore(chunks)

        # Step 3: Generate summary
        summary = self.summary_agent.generate_summary(chunks)

        # Step 4: Extract actions
        context = self.vector_db.get_context(summary)
        actions = self.action_agent.extract_actions(context, summary)

        # Step 5: Identify risks
        risks = self.risk_agent.identify_risks(context, summary, actions)

        return {
            'summary': summary,
            'action_items': actions,
            'open_issues_and_risks': risks
        }
