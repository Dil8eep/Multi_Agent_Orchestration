from langchain_text_splitters import RecursiveCharacterTextSplitter
import re

def clean_text(text: str) -> str:
    """
    Clean and normalize the input text.
    """
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing whitespaces
    text = text.strip()
    return text

def chunk_document(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> list[str]:
    """
    Split the document into chunks for processing.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_text(text)
    return chunks
