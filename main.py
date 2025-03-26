from stats import get_word_count, get_character_count

def main():
    print(f"{get_word_count()} words found in the document")

    char_counts = get_character_count()
    print("Character counts:")
    for char, count in char_counts.items():
        print(f"'{char}': {count}")


main()