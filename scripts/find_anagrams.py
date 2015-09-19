"""
Script to find anagrams given an input word and a filepath to a text file of
known words.

Argparse or Optparse could be used, but no current requirements for optional
flags or features to the script.

"""
from anagram import find_anagrams, load_words_file
import sys


def main(word, filepath):
    valid_words = load_words_file(filepath)
    for anagram in find_anagrams(word, valid_words):
        print anagram


if __name__ == "__main__":
    if len(sys.argv) != 3:
        msg = """
        Invalid arguments specified.
        Usage:
        python find_anagrams.py <word> <filepath>
        """
        print msg
    else:
        main(sys.argv[1], sys.argv[2])
