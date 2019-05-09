"""Takes a word as input and returns its Pig Latin equivalent."""
from src.ch01.practice import VOWELS, ENCODE_ERROR


def encode(word: str) -> str:
    """Check if word starts with vowel, then translate to Pig Latin.

    If a word begins with a consonant, move the consonant to the end of the
    word and add 'ay' to the end of the new word. If a word begins with a
    vowel, add 'way' to the end of the word.

    Args:
        word (str): Word to encode to Pig Latin.

    Returns:
        Encoded Pig Latin word.

    Raises:
        TypeError: If `word` is not a string.

    """
    # Check if word is a string
    if not isinstance(word, str):
        raise TypeError(ENCODE_ERROR)

    # Check if word starts with a vowel.
    if word.lower().startswith(VOWELS):
        # If so, append 'way' and return result.
        return word + 'way'

    # If not, move the consonant to the end of the word, add 'ay', and
    # return the result
    return word[1:] + word[0].lower() + 'ay'


def main():
    """Demonstrate Pig Latin encoder."""
    print("This is a Pig Latin encoder.")

    while True:
        word = input("\nEnter a word to encode to Pig Latin: ")
        print(f"\nTranslation: {encode(word)}")

        retry = input("\nTry again? (Y/N) ")
        if retry.lower().startswith('n'):
            print("\nThank you, and good bye.")
            break


if __name__ == '__main__':
    main()
