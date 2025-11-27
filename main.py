def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")

main()  