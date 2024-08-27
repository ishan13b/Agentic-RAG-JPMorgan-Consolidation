# Index the data 
# Build summarization with recursion
# Build QA with routing


import os
from llama_index.core import SimpleDirectoryReader
from tqdm import tqdm 

def process_all_pdfs_in_directory(directory):
    # data = []
    file_paths = []
    # List all files in the given directory
    for filename in tqdm(os.listdir(directory)):
        # Check if the file is a PDF
        if filename.endswith('.PDF'):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            file_paths.append(file_path)

    file_data = SimpleDirectoryReader(input_files=file_paths).load_data()
    return file_data


# Driver code
# Specify the directory containing PDF files
if __name__ == '__main__':
    pdf_directory = 'data_files'

    data = process_all_pdfs_in_directory(pdf_directory)

    print(len(data))
