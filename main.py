import sys
# the line below imports commands from the stats.py module
from stats import get_word_count, get_character_count, char_sort_by_number#, filepath

#1. use TRY to take the sys.argy and evaluate if there IS a second parameter (1)
#2. If there is NOT, use a ERROR message to print a usage explanation
# - maybe if sys.argy len==1, give error, else use sys.argy[1] for filepath?
#3. If there IS, use the argy[1] as the filepath - since the lifting is done in 
#    functions in stats.py, bring the functions in should work.


filepath = ""
if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]


# main is set to print a number of words, and a character count.
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(filepath)} total words")
    print("--------- Character Count -------")
    char_unsorted = get_character_count(filepath)
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