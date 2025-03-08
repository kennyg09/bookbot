from stats import get_num_words, get_chars_dict, get_sorted

def get_book_text(path):
    with open(path) as f :
        file_contents = f.read()
        return file_contents

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    pp_sort = get_sorted(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_data in pp_sort:
        if char_data['character'].isalpha():
            print(f"{char_data['character']}: {char_data['count']}")
    print("============= END ===============")



if __name__ == '__main__':
    main()
