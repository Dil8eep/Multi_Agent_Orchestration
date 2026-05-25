from pydantic import BaseModel
from typing import List, Optional

class ActionItem(BaseModel):
    task: str
    owner: Optional[str] = None
    dependencies: Optional[str] = None
    deadline: Optional[str] = None

class DocumentAnalysisOutput(BaseModel):
    summary: str
    action_items: List[ActionItem]
    open_issues_and_risks: List[str]
