from llm_translate.utils.text_splitter import get_first_n_words, split_text_to_chunks
import pytest

def test_get_first_n_words():
    # Test with a regular string
    assert get_first_n_words("This is a test sentence.", 3) == "This is a"

    # Test with fewer words than requested
    assert get_first_n_words("Short sentence.", 5) == "Short sentence."

    # Test with exactly the number of words requested
    assert get_first_n_words("Exact number of words.", 4) == "Exact number of words."

    # Test with n_words = 0
    assert get_first_n_words("This should return empty.", 0) == ""

    # Test with empty string
    assert get_first_n_words("", 5) == ""



import pytest

def test_split_text_to_chunks_basic():
    text = "This is a simple sentence. Another sentence follows."
    max_length = 5
    expected_output = [
        "This is a simple sentence.",
        "Another sentence follows."
    ]
    assert split_text_to_chunks(text, max_length) == expected_output

def test_split_text_to_chunks_with_comma():
    text = "This is a sentence, with a comma. And this is another sentence! Some text"
    max_length = 6
    expected_output = [
        "This is a sentence,",
        "with a comma.",
        "And this is another sentence!",
        "Some text"
    ]
    assert split_text_to_chunks(text, max_length) == expected_output


def test_split_text_to_chunks_without_punctuation():
    text = "This is a sentence with no punctuation and it keeps going"
    max_length = 5
    expected_output = [
        "This is a sentence with",
        "no punctuation and it keeps",
        "going"
    ]
    assert split_text_to_chunks(text, max_length) == expected_output

def test_split_text_to_chunks_max_length():
    text = "This is a sentence. Another sentence."
    max_length = 6
    expected_output = [
        "This is a sentence. Another sentence."
    ]
    assert split_text_to_chunks(text, max_length) == expected_output


def test_split_text_to_chunks_edge_case():
    text = "Hello."
    max_length = 1
    expected_output = ["Hello."]
    assert split_text_to_chunks(text, max_length) == expected_output

def test_split_text_to_chunks_mixed_punctuation():
    text = "This sentence has, commas, and full stops. And questions? Exclamations!"
    max_length = 5
    expected_output = [
        "This sentence has, commas,",
        "and full stops. And questions?",
        "Exclamations!"
    ]
    assert split_text_to_chunks(text, max_length) == expected_output

def test_split_text_to_chunks_long_text():
    text = "This is a very long sentence that will be split into multiple chunks based on the max length provided. Let's see how it performs."
    max_length = 10
    expected_output = [
        "This is a very long sentence that will be split",
        "into multiple chunks based on the max length provided.",
        "Let's see how it performs."
    ]
    assert split_text_to_chunks(text, max_length) == expected_output

def test_split_text_to_chunks_empty_text():
    text = ""
    max_length = 5
    expected_output = [""]
    assert split_text_to_chunks(text, max_length) == expected_output

def test_split_text_to_chunks_no_punctuation_split_at_length():
    text = "This is a test text with no punctuation that exceeds the max length."
    max_length = 5
    expected_output = [
        "This is a test text",
        "with no punctuation that exceeds",
        "the max length."
    ]
    assert split_text_to_chunks(text, max_length) == expected_output


def test_split_text_to_chunks_exact_match_length():
    text = "Exact match length sentence."
    max_length = 4
    expected_output = [
        "Exact match length sentence."
    ]
    assert split_text_to_chunks(text, max_length) == expected_output
def test_split_text_to_chunks_exact_match_length_last_dot():
    text = "Exact match length sentence."
    max_length = 4
    expected_output = [
        "Exact match length sentence."
    ]
    assert split_text_to_chunks(text, max_length) == expected_output

def test_split_text_to_chunks_exact_match_length_last_comma():
    text = "Exact match length sentence,"
    max_length = 4
    expected_output = [
        "Exact match length sentence,"
    ]
    assert split_text_to_chunks(text, max_length) == expected_output
