import pytest
from generate_jalons import extract_short_title

def test_extract_short_title_comma():
    assert extract_short_title("Logique formelle, connecteurs") == "Logique formelle"

def test_extract_short_title_parentheses():
    assert extract_short_title("Quantification (\\forall, \\exists)") == "Quantification"

def test_extract_short_title_colon():
    assert extract_short_title("Test : something") == "Test"

def test_extract_short_title_none():
    assert extract_short_title("Logique formelle") == "Logique formelle"

def test_extract_short_title_multiple():
    assert extract_short_title("Logique, formelle: connecteurs") == "Logique"

def test_extract_short_title_whitespace():
    assert extract_short_title("  Logique formelle  ") == "Logique formelle"
