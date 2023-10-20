import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def extract_text_from_epub(epub_path, txt_path):
    # Load the EPUB file
    book = epub.read_epub(epub_path)

    full_text = ""

    # Extract content from each item in the EPUB file
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.content, 'html.parser')
            full_text += soup.get_text() + "\n\n"

    # Save the extracted content to a text file
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(full_text)

if __name__ == "__main__":
    # Change these paths as needed
    epub_file_path = 'book/horcynus.epub'
    txt_file_path = 'orca.txt'

    extract_text_from_epub(epub_file_path, txt_file_path)
    print(f"Text extracted to {txt_file_path}")
