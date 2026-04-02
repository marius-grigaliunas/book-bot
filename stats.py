def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def get_word_count(text: str):
    split_text = text.split()
    return len(split_text)

def get_char_usage(text: str):
    char_dict: dict[str, int] = {}

    for letter in text.lower():
        
        if not char_dict.get(letter):
            char_dict.update({letter: 1})
        else:
            char_dict[letter]+=1
    
    return char_dict