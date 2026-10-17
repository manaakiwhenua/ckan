import pytest

from ckan.lib import webassets_tools


@pytest.fixture
def library(monkeypatch, tmp_path):
    monkeypatch.setitem(
        webassets_tools._library_paths, "my-lib", str(tmp_path)
    )
    return str(tmp_path)


@pytest.mark.parametrize("filename", [
    "icon.svg", "vendor/images/icon.PNG", "fonts/font.woff2",
])
def test_find_library_file_static(library, filename):
    assert webassets_tools.find_library_file(f"my-lib/{filename}") == (
        library, filename
    )


@pytest.mark.parametrize("path", [
    "my-lib/style.css",
    "my-lib/script.js",
    "my-lib/webassets.yml",
    "my-lib/",
    "my-lib",
    "other-lib/icon.svg",
])
def test_find_library_file_rejected(library, path):
    assert webassets_tools.find_library_file(path) is None
