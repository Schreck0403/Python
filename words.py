def print_upper_words(words):
    """Print each word in all uppercase."""
    for word in words:
        print(word.upper())

def print_upper_words_starting_with(words, must_start_with):
    """Print words that start with one of the specified letters in all uppercase."""
    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())

if __name__ == "__main__":
    words = ["hello", "hey", "goodbye", "yo", "yes"]

    print("All words in uppercase:")
    print_upper_words(words)

    letters_to_match = {"h", "y"}
    print("Words starting with letters 'h' or 'y' in uppercase:")
    print_upper_words_starting_with(words, letters_to_match)
