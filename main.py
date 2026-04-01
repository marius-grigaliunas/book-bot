def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()

    return(file_contents)

def get_word_count(book_text: str):
    split_text = book_text.split()

    return len(split_text)

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book_text)

    print(f"Found {word_count} total words")

main()