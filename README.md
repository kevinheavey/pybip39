# pybip39

`pybip39` is a fast Python library for
[BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)
Bitcoin HD wallet mnemonic phrases. It supports multiple languages
and allows for seed phrases of 12 to 24 words. `pybip39` calls the Rust library
[tiny-bip39](https://github.com/maciejhirsz/tiny-bip39)
under the hood, thus benefitting from Rust's speed and safety.

[Online Docs](https://kevinheavey.github.io/pybip39/api_reference.html).

## Installation

`pip install pybip39`

Note: requires Python >= 3.7.

## Usage:

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

## Development

### Setup

1. Install [poetry](https://python-poetry.org/)
2. Install dev dependencies:

```
poetry install
```

3. Activate the poetry shell:

```sh
poetry shell
```

### Testing

1. Run `maturin develop` to compile the Rust code.
2. Run `make fmt`, `make lint`, and `make test`.
