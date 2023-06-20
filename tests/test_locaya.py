from locaya.locaya import Locaya
from locaya.language import Language
from locaya.loader.yaml import YamlLoader


def test_locaya_with_yaml_loader():
    expected_language = Language("test", "Test language", "Respirens", "Test description")
    locaya = Locaya(YamlLoader("fixtures"))
    locaya.load()
    assert locaya.get("test") is not None
    assert locaya.get("test").language == expected_language
