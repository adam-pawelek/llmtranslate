import os

import pytest

from llmtranslate import get_language_info
from llmtranslate.benchmark.format_benchmark_output import create_readme_format


def test_create_readme_format():
    model_name = "claude-3-5-sonnet-20240620"
    language_info = get_language_info("en")

    benchmark_results = [
        {
            "supported_language": True,
            "language_name": language_info["language_name"],
            "ISO_639_1_code": language_info["ISO_639_1_code"],
        },
        {
            "supported_language": False,
            "language_name": language_info["language_name"],
            "ISO_639_1_code": language_info["ISO_639_1_code"],
        }
    ]
    new_readme_format = create_readme_format(model_name, benchmark_results)
    # With this path construction:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "create_readme_format_test_text.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()


    assert new_readme_format == content
