# BookBot

### Small CLI tool that analyzes plain-text books(or any sort of plain text files) and gives you total word count and character frequencies

## Context

### BookBot is my first [Boot.dev](https://www.boot.dev) project!
And my first python CLI tool. 

## Features

- main.py
CLI entry: requires one argument, the path to a book file. Loads text, computes word count and per-character counts, prints a framed report. Only alphabetic characters are printed
- stats.py
get_book_text reads the file; 
get_word_count uses whitespace splitting; 
get_char_usage lowercases and tallies every character (including spaces/punctuation in the dict); 
sorted_list_from_dict turns the dict into a list of {"char", "num"} and sorts by frequency descending.

Also in this repository, you can find another backed up copy of:
Frankenstein
Moby Dick
Pride and Prejudice