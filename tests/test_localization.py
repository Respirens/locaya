from typing import Final

from locaya.localization import load

TEST_LOCALIZATION_FILE: Final[str] = "test_localization.yml"


def test_localization_loading():
    with open(TEST_LOCALIZATION_FILE) as file:
        localization = load(file.read(), strict=True)
    expected_code = "test_code"
    expected_name = "Test Name"
    expected_author = "Respirens"
    expected_description = "For testing only"
    expected_variables = {"var1": "Variable 1"}
    expected_str1 = "This is string with Variable 1"
    expected_str2 = "This is string without $var1"
    assert localization.meta.code == expected_code
    assert localization.meta.name == expected_name
    assert localization.meta.author == expected_author
    assert localization.meta.description == expected_description
    assert localization.meta.variables == expected_variables
    assert localization("str1") == expected_str1
    assert localization("str2") == expected_str2
