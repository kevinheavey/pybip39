# pybip39

`pybip39` is a fast Python library for
[BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)
Bitcoin HD wallet mnemonic phrases.

It is merely a wrapper around the
[tiny-bip39](https://github.com/maciejhirsz/tiny-bip39)
Rust library.

## Installation

`pip install pybip39`

Note: requires Python >= 3.7.

## Example:

```python
from pybip39 import Mnemonic, Seed

mnemonic = Mnemonic()
# Get the phrase
phrase = mnemonic.phrase
print(f"phrase: {phrase}")
# Get the HD wallet seed
seed = Seed(mnemonic, "")
# get the HD wallet seed as raw bytes
seed_bytes = bytes(seed)
print(seed_bytes)

```

## Documentation credit

Most of this documentation is copied from
the [tiny-bip39 docs](https://docs.rs/tiny-bip39/latest/bip39/index.html).
