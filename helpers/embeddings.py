from langchain_text_splitters import RecursiveCharacterTextSplitter
import torch
from transformers import AutoTokenizer, AutoModel
from helpers.text_extractor import get_all_text

def split_into_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 800, chunk_overlap = 0, length_function = len)
    texts = text_splitter.create_documents([text])
    chunks = [text.page_content for text in texts]
    return chunks

def create_bge_embeddings(chunks):
    model_name = "BAAI/bge-small-en-v1.5"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    inputs = tokenizer(chunks, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)  # Mean pooling

    return embeddings

def generate_embeddings_from_pdf(text):
    text = get_all_text()
    chunks = split_into_chunks(text)
    embeddings = create_bge_embeddings(chunks)
    save_embeddings(embeddings)


def save_embeddings(embeddings):
    file_path = "../pkl/embeddings.pkl"
    with open(file_path, 'wb') as file:
        pickle.dump(embeddings, file)
    print(f'Embeddings saved to {file_path}')
