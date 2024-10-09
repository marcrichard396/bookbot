def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    num_word = num_words(text)
    char_count = count_characters(text)
    print_report(book_path, num_word, char_count)
    return None


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def num_words(text):
    words = text.split()
    return(len(words))


def count_characters(text):
    char_count = {}
    lowered_text = text.lower()

    for char in lowered_text:
        try:
            char_count[char] += 1
        except KeyError:
            char_count[char] = 1 
    return char_count


def sort_on(dict):
    return dict["num"]


def print_report(doc_path, num_word, char_count):

    alpha_char_count = []

    for key in char_count:
        if key.isalpha() == True:
            alpha_char_count.append({"char": key, "num": char_count[key]})
    
    alpha_char_count.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of the {doc_path} ---")
    print(f"{num_word} words found in the document\n")
    for dict in alpha_char_count:
        print(f"The {dict['char']} character was found {dict['num']} times")
    print("--- End report ---")
    return None


main()