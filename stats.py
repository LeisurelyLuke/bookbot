def get_num_words(text):
    words = text.split()
    return len(words) 


def get_chars_dict(text):
    chars = {}
    for c in text:
        lower = c.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars


def sort_on(c):
    return c["count"] #sorts on the "count" value inside dictionaries within sorted__character_list


def chars_dict_to_sorted_list(chars_dict):
    sorted_chars = []
    for character in chars_dict:
        if character.isalpha():
            sorted_chars.append({"character": character, "count": chars_dict[character]})
    sorted_chars.sort(key=sort_on, reverse=True)
    return sorted_chars