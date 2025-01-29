import pytest

from llmtranslate import get_language_info


@pytest.mark.parametrize(
    "identifier,expected",
    [
        # Valid inputs
        ("English", {
            "language_name": "English",
            "ISO_639_1_code": "en",
            "ISO_639_2_code": "eng",
            "ISO_639_3_code": "eng",
        }),
        ("en", {
            "language_name": "English",
            "ISO_639_1_code": "en",
            "ISO_639_2_code": "eng",
            "ISO_639_3_code": "eng",
        }),
        ("spa", {
            "language_name": "Spanish",
            "ISO_639_1_code": "es",
            "ISO_639_2_code": "spa",
            "ISO_639_3_code": "spa",
        }),
        ("eng", {
            "language_name": "English",
            "ISO_639_1_code": "en",
            "ISO_639_2_code": "eng",
            "ISO_639_3_code": "eng",
        }),
        # Invalid inputs
        ("xyz", None),
        ("", None),
        ("123", None),
    ],
)
def test_get_language_info(identifier, expected):
    assert get_language_info(identifier) == expected