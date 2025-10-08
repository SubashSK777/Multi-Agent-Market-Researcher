import streamlit as st
import re
import sys
from crewai import Crew, Process
from agents import reporting_analyst, market_research_analyst, financial_analyst
from tasks import reporting_analysis, market_analysis, financial_analysis

# Stream sys output to Streamlit
class StreamToContainer:
    def __init__(self, container):
        self.container = container
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']
        self.color_index = 0
    
    def write(self, data):
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)
        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.container.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []

# Streamlit UI
st.header("Financial & Market Research Multi-Agent")
st.subheader("Generate a Financial and Market Research Analysis Report!")

with st.form("form"):
    company = st.text_input("Enter the name of the Company", key="company")
    submitted = st.form_submit_button("Submit")

if submitted:
    with st.status("🤖 Agents at work...", expanded=True, state="running") as status:
        with st.container(height=300):
            sys.stdout = StreamToContainer(st)
            crew = Crew(
                agents=[financial_analyst, market_research_analyst, reporting_analyst],
                tasks=[financial_analysis, market_analysis, reporting_analysis],
                process=Process.sequential,
                verbose=True
            )
            result = crew.kickoff(inputs={"company": company})
        
        status.update(label="✅ Your Report is ready", state="complete", expanded=False)

    st.subheader("Financial and Market Research Report")
    st.markdown(result)
