filepath = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def get_word_count():
    output = get_book_text(filepath)
    word_list = output.split() 
    num_words = len(word_list)
    return num_words

# to make a function call get_character_count, I need to:
# 1. in STATS, break the book text into a dictionary of characters
# 2. Convert any upper case characters into lower case characters
# 3. set up the dictionary so that each instance of a character += an individual character counter in the dictionary
# 4. return those results to the main.py
# 5. Print those results using a get_character_count function call.
def get_character_count():
    char_count = {}
    text = get_book_text(filepath).lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
        
        