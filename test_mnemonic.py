from pybip39 import Mnemonic


def test_back_to_back() -> None:
    m1 = Mnemonic(12, "en")
    m2 = Mnemonic.from_phrase(m1.phrase, "en")
    m3 = Mnemonic.from_entropy(m1.entropy, "en")
    assert m1.entropy == m2.entropy
    assert m1.entropy == m3.entropy
    assert m1.phrase == m2.phrase
    assert m1.phrase == m3.phrase
