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

def sorted_list_from_dict(letter_dict: dict):
    new_list = []

    for letter, frequency in letter_dict.items():
        new_list.append({
            "char": letter,
            "num": frequency
        })
    
    def sort_on_frequency(dict_list: list):
        return dict_list["num"]

    new_list.sort(reverse=True, key=sort_on_frequency)

    return new_list
