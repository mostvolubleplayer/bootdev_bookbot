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




