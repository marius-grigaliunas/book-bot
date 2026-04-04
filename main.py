import sys
from stats import get_book_text, get_word_count, get_char_usage, sorted_list_from_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1] 
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    characters = get_char_usage(text)

    sorted_characters = sorted_list_from_dict(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_characters:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()