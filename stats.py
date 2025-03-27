# filepath is currently hardcoded to the frankenstein.txt file 
#  inside the book directory.
filepath = "./books/frankenstein.txt"

# get_book_text reads the book in the filepath and returns the 
#  contents as a string in the file_contents variable.
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

# get_word_count takes whatever book is hardcoded to filepath, 
#  counts the words, and returns the number of words
def get_word_count():
    output = get_book_text(filepath)
    word_list = output.split() 
    num_words = len(word_list)
    return num_words

# get_character_count is set up to use get_book_text, convert those 
#  characters to all lower case, and then add and count each character.
def get_character_count():
    char_count = {}
    text = get_book_text(filepath).lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# below is how to sort a dictionary by number
# define a new function

def char_sort_by_number(char_dict):
    #create an empty list to store the dictionaries
    sorted_char_list = []
    #convert each key-value pair in the dictionary to 
    #a dictionary and add it to the list:
    for char, count in char_dict.items():
        sorted_char_list.append({"char": char, "count": count})
    #define a sorting helper:
    def sort_on(dict_item):
        return dict_item["count"]
    #perform the sort, indescending order - the sort_on defines the keyed item
    sorted_char_list.sort(reverse=True, key=sort_on)
    #return the sorted character list
    return sorted_char_list


        