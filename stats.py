def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()

def get_num_words():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")

def get_unique_character_count():
    unique_character_dict = {}
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    for character in book_text:
        lower_character = character.lower()
        if lower_character in unique_character_dict:
            unique_character_dict[lower_character] += 1
        else:
            unique_character_dict[lower_character] = 1
    print(unique_character_dict)