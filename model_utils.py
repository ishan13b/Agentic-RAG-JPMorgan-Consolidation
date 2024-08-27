import os
from llama_index.llms.groq import Groq

os.environ["GROQ_API_KEY"] = "<YOUR_TOKEN>"



llm = Groq(model="llama-3.1-8b-instant")
llm_70b = Groq(model="llama-3.1-70b-versatile")