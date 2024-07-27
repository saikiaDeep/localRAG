from helpers.pdf_downloader import download_from_storage
from helpers.embeddings import generate_embeddings_from_pdfs

def main():
    download_from_storage()
    generate_embeddings_from_pdfs()

if __name__ == "__main__":
    main()