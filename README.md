
# Local RAG System

This repository contains a basic Retrieval-Augmented Generation (RAG) system designed to be used locally. 

## Getting Started

Follow these instructions to set up and run the system:

1. **Install Dependencies**

   Ensure you have `pip` installed, then run the following command to install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

2. **Generate Embeddings**

   Run `creator.py` to generate embeddings needed for the RAG system:

   ```bash
   python creator.py
   ```

3. **Start the FastAPI Server**

   Once embeddings are generated, start the FastAPI server with:

   ```bash
   uvicorn app:app --reload
   ```

   The server will be available at `http://127.0.0.1:8000`.

