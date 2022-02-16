from pybip39 import Mnemonic, MnemonicType, Language


def test_back_to_back() -> None:
    m1 = Mnemonic()
    m2 = Mnemonic.from_phrase(m1.phrase)
    m3 = Mnemonic.from_entropy(m1.entropy)
    assert m1.entropy == m2.entropy
    assert m1.entropy == m3.entropy
    assert m1.phrase == m2.phrase
    assert m1.phrase == m3.phrase


def test_from_entropy() -> None:
    entropy = bytes(
        [
            0x33,
            0xE4,
            0x6B,
            0xB1,
            0x3A,
            0x74,
            0x6E,
            0xA4,
            0x1C,
            0xDD,
            0xE4,
            0x5C,
            0x90,
            0x84,
            0x6A,
            0x79,
        ]
    )
    phrase = "crop cash unable insane eight faith inflict route frame loud box vibrant"

    mnemonic = Mnemonic.from_entropy(entropy)

    assert phrase == mnemonic.phrase


def test_from_phrase() -> None:
    entropy = bytes(
        [
            0x33,
            0xE4,
            0x6B,
            0xB1,
            0x3A,
            0x74,
            0x6E,
            0xA4,
            0x1C,
            0xDD,
            0xE4,
            0x5C,
            0x90,
            0x84,
            0x6A,
            0x79,
        ]
    )
    phrase = "crop cash unable insane eight faith inflict route frame loud box vibrant"

    mnemonic = Mnemonic.from_phrase(phrase)

    assert entropy == mnemonic.entropy


def test_str() -> None:
    mnemonic = Mnemonic(MnemonicType.Words15)

    assert mnemonic.phrase == str(mnemonic)


def test_hex() -> None:
    entropy = bytes(
        [
            0x03,
            0xE4,
            0x6B,
            0xB1,
            0x3A,
            0x74,
            0x6E,
            0xA4,
            0x1C,
            0xDD,
            0xE4,
            0x5C,
            0x90,
            0x84,
            0x6A,
            0x79,
        ]
    )

    mnemonic = Mnemonic.from_entropy(entropy)

    assert mnemonic.hex() == "03e46bb13a746ea41cdde45c90846a79"
    assert bytes(entropy) == bytes.fromhex(mnemonic.hex())


def test_bytes() -> None:
    entropy = bytes(
        [
            0x03,
            0xE4,
            0x6B,
            0xB1,
            0x3A,
            0x74,
            0x6E,
            0xA4,
            0x1C,
            0xDD,
            0xE4,
            0x5C,
            0x90,
            0x84,
            0x6A,
            0x79,
        ]
    )
    mnemonic = Mnemonic.from_entropy(entropy)
    assert bytes(mnemonic) == entropy
