import pytest
from word_freq import top_words

def test_top_words_normal(tmp_path):
    f = tmp_path / "sample.txt"
    f.write_text("the cat sat on the mat. the cat was happy.")
    result = top_words(str(f), n=2)
    assert result == [("the", 3), ("cat", 2)]

def test_top_words_empty_file(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("")
    with pytest.raises(ValueError):
        top_words(str(f))

def test_top_words_missing_file():
    with pytest.raises(FileNotFoundError):
        top_words("this_file_does_not_exist.txt")
