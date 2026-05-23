import pytest
from generate_jalons import generate_links

def test_generate_links():
    jalons_list = [
        {'filename': 'Jalon 1 (Logique formelle).md'},
        {'filename': 'Jalon 2 (Méthodes de raisonnement).md'},
        {'filename': 'Jalon 3 (Quantification).md'}
    ]

    # Test first element (index=0)
    result_first = generate_links(None, jalons_list, 0)
    assert result_first == "**Suivant** : [[Jalon 2 (Méthodes de raisonnement)]]"

    # Test middle element (index=1)
    result_middle = generate_links(None, jalons_list, 1)
    assert result_middle == "**Précédent** : [[Jalon 1 (Logique formelle)]] | **Suivant** : [[Jalon 3 (Quantification)]]"

    # Test last element (index=2)
    result_last = generate_links(None, jalons_list, 2)
    assert result_last == "**Précédent** : [[Jalon 2 (Méthodes de raisonnement)]]"

    # Test empty/single element
    result_single = generate_links(None, [{'filename': 'Jalon 1.md'}], 0)
    assert result_single == ""
