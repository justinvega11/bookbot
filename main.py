from stats import get_num_words, get_letter_count,print_dict
from sys import argv, exit

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path to book>")
        exit(1)
        return

    book_path = argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    text_lowercase = text.lower()
    letter_count = get_letter_count(text_lowercase)

    print_dict(letter_count,book_path,num_words)
    #print(letter_count)
    #print(f"{num_words} words found in the document")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()