from llama_index.core import SummaryIndex
from index_data import process_all_pdfs_in_directory
from model_utils import llm, llm_70b
from llama_index.core import Settings
# from llama_index.core import VectorStoreIndex



Settings.llm = llm

pdf_directory = 'data_files'

data = process_all_pdfs_in_directory(pdf_directory)

index = VectorStoreIndex.from_documents(data)
query_engine = index.as_query_engine(similarity_top_k=3)

response = query_engine.query("Tell me the full form of N.A. in JPMorgan Chase Bank N.A.")
print(response)

# summary_index = SummaryIndex.from_documents(data)
# summary_engine = summary_index.as_query_engine()

# response = summary_engine.query(
#     "Given your assessment of this article, what is the full form of NA in JPMorgan Bank N.A.?"
# )
