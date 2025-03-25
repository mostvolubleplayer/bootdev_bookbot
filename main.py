filepath = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    output = get_book_text(filepath)
    print(output)

main()