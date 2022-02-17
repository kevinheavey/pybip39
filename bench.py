import mnemonic
import pybip39


def test_pybip39_mnemonic(benchmark):
    benchmark(pybip39.Mnemonic)


def test_mnemonic_mnemonic(benchmark):
    benchmark(mnemonic.Mnemonic, "english")


def test_pybip39_words(benchmark):
    mnemo = pybip39.Mnemonic()
    benchmark(lambda: mnemo.phrase)


def test_mnemonic_words(benchmark):
    mnemo = mnemonic.Mnemonic("english")
    benchmark(mnemo.generate)


def _pybip39_mnemo_to_seed_bytes(mnemo: pybip39.Mnemonic) -> bytes:
    seed = pybip39.Seed(mnemo, "")
    return bytes(seed)


def _mnemonic_mnemo_to_seed_bytes(mnemo: mnemonic.Mnemonic) -> bytes:
    words = mnemo.generate()
    return mnemo.to_seed(words)


def test_pybip39_seed(benchmark):
    mnemo = pybip39.Mnemonic()
    benchmark(_pybip39_mnemo_to_seed_bytes, mnemo)


def test_mnemonic_seed(benchmark):
    mnemo = mnemonic.Mnemonic("english")
    benchmark(_mnemonic_mnemo_to_seed_bytes, mnemo)
