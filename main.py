from stats import (
    get_num_words,
    get_chars_dict,
    chars_dict_to_sorted_list
    )


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) #provides book text as a string
    num_words = get_num_words(text) #calls word-counting function from stats.py
    chars_dict = get_chars_dict(text) #calls function that creates a dictionary of characters and their counts
    sorted_chars_list = chars_dict_to_sorted_list(chars_dict) #calls function that makes a list of dictionaries and sorts them by count (descending)
    print_report(book_path, num_words, sorted_chars_list)


def print_report(book_path, num_words, sorted_chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -----------")
    for d in sorted_chars_list: #d stands for each dictionary inside the list
        print(f"{d["character"]}: {d["count"]}") #prints character and its count set in sorted_chars list
    print("============= END ===============")


def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()


main()