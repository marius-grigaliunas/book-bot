from stats import get_book_text, get_word_count, get_char_usage

def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(text)
    characters = get_char_usage(text)

    print(f"Found {word_count} total words")
    print(characters)
main()