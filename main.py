
# the line below imports commands from the stats.py module
from stats import get_word_count, get_character_count, filepath, char_sort_by_number

# main is set to print a number of words, and a character count.
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count()} total words")
    print("--------- Character Count -------")
    char_unsorted = get_character_count()
    sorted_char = char_sort_by_number(char_unsorted)
    for char_dict in sorted_char:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")  


#OLD    print(f"{get_word_count()} words found in the document")

#OLD char_counts = get_character_count()
#OLD    for char, count in char_counts.items():
#OLD        print(f"'{char}': {count}")  


main()