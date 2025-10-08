from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import os

load_dotenv()

# Optional: If you have SERPER_API_KEY, otherwise remove the line
# os.environ["SERPER_API_KEY"] = os.environ.get("SERPER_API_KEY")

# Tool for searching on Google
tool = SerperDevTool()
