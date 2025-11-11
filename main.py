from stats import get_num_words, get_character_count, sort_dict
import sys

def __main__():
    sys_args = sys.argv
    if len(sys_args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys_args[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(path_to_book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count_dict = get_character_count(path_to_book)
    sorted_counts = sort_dict(char_count_dict)
    for count in sorted_counts:
        print(f"{count["char"]}: {count["num"]}")
    
    
__main__()