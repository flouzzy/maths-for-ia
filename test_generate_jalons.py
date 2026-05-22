import pytest
from generate_jalons import get_custom_content

def test_get_custom_content_with_108():
    expected = "Notions liées : [[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L^2)]] et [[Jalon 105 (Opérateurs adjoints)]]."
    assert get_custom_content("108") == expected
    assert get_custom_content("Jalon 108") == expected

def test_get_custom_content_without_108():
    assert get_custom_content("107") == ""
    assert get_custom_content("Jalon 1") == ""
    assert get_custom_content("10") == ""
