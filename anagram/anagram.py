"""
Utility methods for finding anagrams of a given word.

Sorting Algorithm:
    To find all possible anagrams of a word, we can simply sort the
    characters in that word alphabetically.  For example:
        'time' --> 'eimt'
    If we sort all the words we're comparing too, then we'll be able to
    check for equality.  If they're equal, then they're anagrams.
        'mite' --> 'eimt'  Anagram of 'time'
        'emit' --> 'eimt'  Anagram of 'time'
        'ball' --> 'abll'  Not an anagram of 'time'

    This algorithm requires minimal memory usage because we can iterate
    over the list of known words. We are performing at worst case N+1 sorts
    where N is the number of known words in the list.  We can reduce this
    number by only checking similar length words ('time' and 'continuum')
    can never be an anagram, so we don't need to sort 'continuum'.

    We're performing N sorts of O(n log n), where N is the number of words
    and n is the length of each word.  We don't require memory as we can
    process each item and yield our answers as we go.


Permutations Algorithm:
    Another algorithm is find all the possible letter permutations of a word.
    With those permutations in memory (a set or a dict), then you can simply
    iterate line by line over the file and get O(1) lookup time to see if it
    is in the possible anagrams list.  This algorithm has the downside of
    requiring at worst case a set of strings, n! in length, and each item taking
    n bytes.  The set construction time would be O(n!) where n is the len(word).

"""
from itertools import permutations


def load_words_file(filepath):
    """
    Opens a file and yields line by line.  It uses rstrip() to remove whitespace
    and newlines.
    """
    with open(filepath) as f:
        for line in f:
            yield line.rstrip()  # We chomp off the trailing '\n' if needed


def get_permutations(word):
    """
    Returns a set of all possible letter combinations of a word. Use caution as
    this method has a worst case of returning n! items where n is the len(word).

    Examples
    --------
    >>> get_permutations('car')
    {'acr', 'arc', 'car', 'cra', 'rac', 'rca'}
    """
    if word is None:
        return None
    return set(''.join(p) for p in permutations(word))


def sort_word(word):
    """
    Sorts a string alphabetically by its characters

    Raises
    ------
    TypeError:
        If the word is not a string

    Examples
    --------
    >>> sort_word('time')
    'eimt'
    >>> sort_word('mite')
    'eimt'
    >>> sort_word('')
    ''
    >>> sort_word(None)
    None
    >>> sort_word(1234)
    Traceback (most recent call last):
    ...
    TypeError: sort_word accepts a string, <type 'int'> provided

    """
    if word is None:
        return None
    if not isinstance(word, str):
        msg = 'sort_word accepts a string, {} provided'
        raise TypeError(msg.format(type(word)))
    return ''.join(sorted(word))


def find_anagrams(word, valid_words):
    """
    Yields results from the valid words if they are anagrams of the given word.

    This algorithm works by taking the base word and sorting the characters
    alphabetically. Then for each word in our valid_list, we sort it and check
    for equality.  For instance:
        Base: 'time' -> Sorted: 'eimt'
        Word: 'mite' -> Sorted: 'eimt'
        'eimt' == 'eimt' -> 'time' is anagram with 'mite'

    Parameters
    ----------
    word: str
        The word used to find all anagrams
    valid_words: iterable
        The valid words to check against

    Yields
    ------
    word: str
        The next valid word that is an anagram of the input word

    Raises
    ------
    ValueError:
        If word for anagram is None

    Examples
    --------
    >>> list(find_anagrams('time', ['emit', 'time', 'mite', 'car', None]))
    ['emit', 'time', 'mite']
    """
    if word is None or valid_words is None:
        raise ValueError('Must provide a word and valid_words to check against')

    # We only need to sort the base word once
    sorted_base = sort_word(word)

    # Filter generator to words that are not None and same len as original word
    filtered_words = (w for w in valid_words if w and len(w) == len(word))

    # If the sorted characters of A and B match, then they're an anagram
    for w in filtered_words:
        if sort_word(w) == sorted_base:
            yield w