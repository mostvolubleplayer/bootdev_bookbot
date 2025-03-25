filepath = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    output = get_book_text(filepath)
    word_list = output.split() 
    num_words = len(word_list)
    print(f"{num_words} words found in the document")

    

main()