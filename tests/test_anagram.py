import pytest
import os
from anagram import find_anagrams, load_words_file, sort_word, get_permutations

CLEAN_DATA_FILE = os.path.join(os.path.dirname(__file__),
                               'data/test_words_clean')

EMPTY_DATA_FILE = os.path.join(os.path.dirname(__file__),
                               'data/test_words_empty')

RSTRIP_DATA_FILE = os.path.join(os.path.dirname(__file__),
                                'data/test_words_rstrip')

MISSING_DATA_FILE = os.path.join(os.path.dirname(__file__),
                                 'data/test_words_missing')


def test_load_words_file_clean():
    words = ['care', 'acre', 'race', 'rack', 'racer']
    assert words == list(load_words_file(CLEAN_DATA_FILE))


def test_load_words_file_empty():
    assert not list(load_words_file(EMPTY_DATA_FILE))


def test_load_words_file_rstrip():
    words = ['care', 'acre', 'race', 'rack', 'racer']
    assert words == list(load_words_file(RSTRIP_DATA_FILE))


def test_load_words_file_not_exists():
    with pytest.raises(IOError):
        list(load_words_file(MISSING_DATA_FILE))


def test_sort_word():
    assert 'eimt' == sort_word('time')
    assert '1234' == sort_word('4321')


def test_sort_word_none():
    assert sort_word(None) is None


def test_sort_word_bad_input():
    with pytest.raises(TypeError):
        sort_word(1234)


def test_get_permutations():
    ans = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    assert get_permutations('abc') == ans


def test_get_permutations_missing_word():
    assert get_permutations(None) is None


def test_find_anagrams():
    ans = ['emit', 'time', 'mite']
    valid_words = ['emit', 'time', 'mite', 'car']
    assert ans == list(find_anagrams('time', valid_words))


def test_find_anagrams_empty_valid_words():
    valid_words = []
    assert [] == list(find_anagrams('time', valid_words))


def test_find_anagrams_missing_word():
    valid_words = ['emit', 'time', 'mite', 'car']
    with pytest.raises(ValueError):
        list(find_anagrams(None, valid_words))


def test_find_anagrams_missing_valid_words():
    with pytest.raises(ValueError):
        list(find_anagrams('time', None))


if __name__ == '__main__':
    pytest.main()