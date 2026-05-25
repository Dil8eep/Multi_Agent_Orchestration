import streamlit as st
from orchestrator import Orchestrator
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY not found in environment variables. Please set it in .env file.")
    st.stop()

orchestrator = Orchestrator(api_key)

st.title("Multi-Agent System for Deep Document Intelligence")

st.markdown("""
This application uses a multi-agent AI system to analyze long unstructured documents and extract:
- Context-aware summary
- Structured action items
- Identified risks and open issues
""")

document = st.text_area("Paste your document here:", height=300)

if st.button("Analyze Document"):
    if document.strip():
        with st.spinner("Processing document..."):
            try:
                result = orchestrator.process_document(document)
                st.success("Analysis complete!")

                st.subheader("Summary")
                st.write(result['summary'])

                st.subheader("Action Items")
                for item in result['action_items']:
                    st.markdown(f"- **Task:** {item.get('task', 'N/A')}")
                    if item.get('owner'):
                        st.markdown(f"  - **Owner:** {item['owner']}")
                    if item.get('dependencies'):
                        st.markdown(f"  - **Dependencies:** {item['dependencies']}")
                    if item.get('deadline'):
                        st.markdown(f"  - **Deadline:** {item['deadline']}")
                    st.markdown("")

                st.subheader("Open Issues and Risks")
                for risk in result['open_issues_and_risks']:
                    st.markdown(f"- {risk}")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a document to analyze.")
