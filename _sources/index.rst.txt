.. pybip39 documentation master file, created by
   sphinx-quickstart on Mon Feb 14 00:09:53 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Introduction
============

``pybip39`` is a fast Python library for
`BIP39 <https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki>`_
Bitcoin HD wallet mnemonic phrases. It supports multiple languages
and allows for seed phrases of 12 to 24 words. ``pybip39`` calls the Rust library
`tiny-bip39 <https://github.com/maciejhirsz/tiny-bip39>`_
under the hood, thus benefitting from Rust's speed and safety.

Installation
^^^^^^^^^^^^

::

    pip install pybip39

.. note:: requires Python >= 3.7.

Usage
^^^^^

::

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


Documentation credit
^^^^^^^^^^^^^^^^^^^^

Most of this documentation is copied from
the `tiny-bip39 docs <https://docs.rs/tiny-bip39/latest/bip39/index.html>`_.


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   self
   api_reference
